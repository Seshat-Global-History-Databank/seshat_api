from .constants import BASE_URL, TOKEN_ENDPOINT
from .exceptions import SeshatAPIException

import importlib
import inflect
import inspect
import requests
import pandas as pd

from typing import Optional
from json import JSONDecodeError

__all__ = ["SeshatAPI"]


class SeshatAPI:
    """
    A class for interacting with the Seshat API.

    Parameters
    ----------
    username : str, optional
        The username to use for authentication.
    password : str, optional
        The password to use for authentication.
    base_url : str, optional
        The base URL of the API. Default is BASE_URL (found in
        seshat_api.constants).
    """

    def __init__(
        self,
        username: Optional[str] = None,
        password: Optional[str] = None,
        base_url: Optional[str] = None,
    ):
        self.base_url = base_url or BASE_URL
        self.username = username
        self.__token = None
        if self.username and password:
            self.__get_token(username, password)

    def __get_token(self, username: str, password: str) -> str:
        """
        Get a token for the API.

        Parameters
        ----------
        username : str
            The username to use for authentication.
        password : str
            The password to use for authentication.

        Returns
        -------
        str
            The token to use for authentication.
        """
        if not self.__token:
            headers = {"User-Agent": "seshat-api-python/1.0"}
            response = requests.post(
                f"{self.base_url}/{TOKEN_ENDPOINT}",
                data={"username": username, "password": password},
                headers=headers,
            )
            response.raise_for_status()
            self.__token = response.json()["token"]

        return self.__token

    def __createException(
        self,
        request: str,
        response: requests.Response,
        message: Optional[str] = None,
    ) -> SeshatAPIException:
        """
        Create an exception from a response.

        Parameters
        ----------
        request : str
            The request that was made.
        response : requests.Response
            The response from the request.
        message : str, optional
            The message to include in the exception.

        Returns
        -------
        SeshatAPIException
            The exception created from the response.
        """
        try:
            data = response.json()
        except JSONDecodeError:
            data = response.text

        return SeshatAPIException(
            response.status_code, data, response.headers, message
        )

    def get(self, endpoint: str, params: dict = None) -> dict:
        """
        Get data from the API.

        Parameters
        ----------
        endpoint : str
            The endpoint to get data from.
        params : dict, optional
            The parameters to use in the request.

        Returns
        -------
        dict
            The data returned from the API.
        """
        url = f"{self.base_url}{endpoint}"
        req_headers = {"User-Agent": "seshat-api-python/1.0"}
        message = None

        # Set authentication headers if token is present
        if self.__token:
            req_headers["Authorization"] = f"Token {self.__token}"

        try:
            response = requests.get(
                url,
                params=params,
                headers=req_headers,
            )
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 403:
                message = "User is not logged in. Did you pass a username and "
                message += "password to the client?"

            if e.response.status_code == 404:
                message = "API endpoint not found"

            if e.response.status_code == 429:
                message = "API rate limit exceeded"

            raise self.__createException(
                endpoint, e.response, message
            ) from None

        # Return JSON-coded data
        return response.json()

    def count(self, endpoint: str, params: Optional[dict] = None) -> int:
        """
        Get the count of items in the API.

        Parameters
        ----------
        endpoint : str
            The endpoint to get the count from.
        params : dict, optional
            The parameters to use in the request.

        Returns
        -------
        int
            The count of items in the API.
        """
        return self.get(endpoint, params)["count"]


def get_variable_classes():
    """
    Get the names of all classes in the API.

    Returns
    -------
    list
        A list of all classes in the API.
    """
    module_paths = [
        'seshat_api.sc',
        'seshat_api.core',
        'seshat_api.general',
        'seshat_api.wf',
        'seshat_api.rt',
        'seshat_api.crisisdb',
    ]
    all_classes = {}
    for module_path in module_paths:
        module = importlib.import_module(module_path)
        members = inspect.getmembers(module)
        classes = [member[0] for member in members if inspect.isclass(member[1])]
        classes.sort()
        all_classes[module_path.split('.')[-1]] = classes
    return all_classes


def get_variable_name(class_name):
    """
    Get the variable name for a Seshat class by converting from plural camel case to singular snake case.

    Parameters
    ----------

    class_name : str
        The class name to get variable name for.

    Returns
    -------
    str
        The variable name for the class.
    """
    p = inflect.engine()
    # Convert from plural to singular if plural
    class_name = p.singular_noun(class_name) or class_name
    # Convert from CamelCase to snake_case
    return ''.join(['_' + i.lower() if i.isupper() else i for i in class_name]).lstrip('_')


def seshat_class_instance(class_name, var):
    """
    Get an instance of a Seshat class by its name.

    Parameters
    ----------
    class_name : str
        The name of the class to get an instance of.
    var : str
        The variable name for the class

    Returns
    -------
    object
        An instance of the class.
    """
    module_paths = ['seshat_api.sc',
                    'seshat_api.core',
                    'seshat_api.general',
                    'seshat_api.wf',
                    'seshat_api.rt',
                    'seshat_api.crisisdb',
                    ]
    module = None
    class_ = None
    for path in module_paths:
        try:
            module = __import__(path, fromlist=[class_name])
            globals()[var] = module
            class_ = getattr(module, class_name)
            break
        except (ImportError, AttributeError):
            continue
    if module is None or class_ is None:
        raise ImportError(f"Module '{class_name}' cannot be found in any of these paths: {', '.join(module_paths)}")
    return class_


def get_frequencies(client, class_names, years, value='present'):
    """
    Get the number of polities (frequency) recorded as having a particular value recorded for a set of variables over a year range.

    Parameters
    ----------
    client : SeshatAPI
        The client to use for the API.
    class_names : list
        The names of the classes to get data from for each variable.
    years : Range
        The range of years to get data for.
    value : str, optional
        The value to get the frequency for. Default is 'present'.

    Returns
    -------
    DataFrame
        A DataFrame with the frequency of each variable having the value across polities over time.
    """
    dataframes = []
    variables = []
    for class_name in class_names:

        # Get the variable name for the class
        var = get_variable_name(class_name)
        variables.append(var)

        # Get the class instance
        instance = seshat_class_instance(class_name, var)(client)

        # Get all data for the class and create a DataFrame
        df = pd.DataFrame(instance.get_all())

        # Extract the polity column as a new DataFrame
        # This gives you the polity data for all polities with the variable
        polities_with_var_df = pd.DataFrame(df['polity'].tolist())

        # Add the variable column to the new polities DataFrame
        polities_with_var_df[var] = df[var]

        dataframes.append(polities_with_var_df)

    # Create a DataFrame to store the frequency of each variable having the value across polities over time
    frequency_df = pd.DataFrame(index=years, columns=variables).infer_objects(copy=False).fillna(0)

    # Count the number of polities with the value for each variable for each year
    for year in years:
        for df, var in zip(dataframes, variables):
            frequency_df.loc[year, var] = len(df[
                (df['start_year'] <= year) &
                (df['end_year'] >= year) &
                (df[var] == value)
            ])
    return frequency_df
