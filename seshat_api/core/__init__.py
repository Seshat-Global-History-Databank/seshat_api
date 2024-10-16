from ..base_model import BaseAPICall
from ..models import (
    MacroRegions,
    Regions,
    NGAs,
    Polities,
    Capitals,
    NGAPolityRelations,
    Countries,
    Sections,
    Subsections,
    VariableHierarchies,
    References,
    Citations,
    Religions,
    CliopatriaShapefiles,
    GADMShapefiles,
    GADMCountries,
    GADMProvinces,
)

__all__ = [
    "Polities",
    "MacroRegions",
    "Regions",
    "NGAs",
    "Capitals",
    "NGAPolityRelations",
    "Countries",
    "Sections",
    "Subsections",
    "VariableHierarchies",
    "References",
    "Citations",
    "Religions",
    "CliopatriaShapefiles",
    "GADMShapefiles",
    "GADMCountries",
    "GADMProvinces",
]


class MacroRegions(BaseAPICall):
    """
    A class for interacting with the macro regions endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.core import MacroRegions
    >>> client = SeshatAPI()
    >>> macro_regions = MacroRegions(client)
    """
    ENDPOINT = "/core/macro-regions"
    SINGLE_MODEL = MacroRegions


class Regions(BaseAPICall):
    """
    A class for interacting with the regions endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.core import Regions
    >>> client = SeshatAPI()
    >>> regions = Regions(client)
    """
    ENDPOINT = "/core/regions"
    SINGLE_MODEL = Regions


class NGAs(BaseAPICall):
    """
    A class for interacting with the NGAs (Natural Geographic Areas) endpoint
    of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.core import NGAs
    >>> client = SeshatAPI()
    >>> ngas = NGAs(client)
    """
    ENDPOINT = "/core/ngas"
    SINGLE_MODEL = NGAs


class Polities(BaseAPICall):
    """
    A class for interacting with the polities endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.core import Polities
    >>> client = SeshatAPI()
    >>> polities = Polities(client)
    """
    ENDPOINT = "/core/polities"
    SINGLE_MODEL = Polities


class Capitals(BaseAPICall):
    """
    A class for interacting with the capitals endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.core import Capitals
    >>> client = SeshatAPI()
    >>> capitals = Capitals(client)
    """
    ENDPOINT = "/core/capitals"
    SINGLE_MODEL = Capitals


class NGAPolityRelations(BaseAPICall):
    """
    A class for interacting with the NGA–polity relations (relations between a
    Natural Geographic Area, NGA, and a polity) endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.core import NGAPolityRelations
    >>> client = SeshatAPI()
    >>> nga_polity_relations = NGAPolityRelations(client)
    """
    ENDPOINT = "/core/nga-polity-relations"
    SINGLE_MODEL = NGAPolityRelations


class Countries(BaseAPICall):
    """
    A class for interacting with the countries endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.core import Countries
    >>> client = SeshatAPI()
    >>> countries = Countries(client)
    """
    ENDPOINT = "/core/countries"
    SINGLE_MODEL = Countries


class Sections(BaseAPICall):
    """
    A class for interacting with the sections endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.core import Sections
    >>> client = SeshatAPI()
    >>> sections = Sections(client)
    """
    ENDPOINT = "/core/sections"
    SINGLE_MODEL = Sections


class Subsections(BaseAPICall):
    """
    A class for interacting with the subsections endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.core import Subsections
    >>> client = SeshatAPI()
    >>> subsections = Subsections(client)
    """
    ENDPOINT = "/core/subsections"
    SINGLE_MODEL = Subsections


class VariableHierarchies(BaseAPICall):
    """
    A class for interacting with the variable hierarchies endpoint of the
    Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.core import VariableHierarchies
    >>> client = SeshatAPI()
    >>> variable_hierarchies = VariableHierarchies(client)
    """
    ENDPOINT = "/core/variable-hierarchies"
    SINGLE_MODEL = VariableHierarchies


class References(BaseAPICall):
    """
    A class for interacting with the references endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.core import References
    >>> client = SeshatAPI()
    >>> references = References(client)
    """
    ENDPOINT = "/core/references"
    SINGLE_MODEL = References


class Citations(BaseAPICall):
    """
    A class for interacting with the citations endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.core import Citations
    >>> client = SeshatAPI()
    >>> citations = Citations(client)
    """
    ENDPOINT = "/core/citations"
    SINGLE_MODEL = Citations


class Religions(BaseAPICall):
    """
    A class for interacting with the religions endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.core import Religions
    >>> client = SeshatAPI()
    >>> religions = Religions(client)
    """
    ENDPOINT = "/core/religions"
    SINGLE_MODEL = Religions


class CliopatriaShapefiles(BaseAPICall):
    """
    A class for interacting with the Cliopatria shapefiles endpoint of the Seshat
    API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.core import CliopatriaShapefiles
    >>> client = SeshatAPI()
    >>> cliopatria_shapefiles = CliopatriaShapefiles(client)
    """
    ENDPOINT = "/core/cliopatria-shapefiles"
    SINGLE_MODEL = CliopatriaShapefiles


class GADMShapefiles(BaseAPICall):
    """
    A class for interacting with the GADM shapefiles endpoint of the Seshat
    API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.core import GADMShapefiles
    >>> client = SeshatAPI()
    >>> gadm_shapefiles = GADMShapefiles(client)
    """
    ENDPOINT = "/core/gadm-shapefiles"
    SINGLE_MODEL = GADMShapefiles


class GADMCountries(BaseAPICall):
    """
    A class for interacting with the GADM countries endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.core import GADMCountries
    >>> client = SeshatAPI()
    >>> gadm_countries = GADMCountries(client)
    """
    ENDPOINT = "/core/gadm-countries"
    SINGLE_MODEL = GADMCountries


class GADMProvinces(BaseAPICall):
    """
    A class for interacting with the GADM provinces endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.core import GADMProvinces
    >>> client = SeshatAPI()
    >>> gadm_provinces = GADMProvinces(client)
    """
    ENDPOINT = "/core/gadm-provinces"
    SINGLE_MODEL = GADMProvinces
