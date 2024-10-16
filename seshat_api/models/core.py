from ._base import BaseModel

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


class Polities(BaseModel):
    """
    A class representing a single Polity object in the Seshat API.

    Parameters
    ----------
    data : dict
        The data to use in the model.
    count : int, optional
        The total count of items in the API.
    name : str, optional
        The name of the API.

    ..
        TODO: Add an example of how to create the object
    """
    pass


class MacroRegions(BaseModel):
    """
    A class representing a single Macro Region object in the Seshat API.

    Parameters
    ----------
    data : dict
        The data to use in the model.
    count : int, optional
        The total count of items in the API.
    name : str, optional
        The name of the API.

    ..
        TODO: Add an example of how to create the object
    """
    pass


class Regions(BaseModel):
    """
    A class representing a single Region object in the Seshat API.

    Parameters
    ----------
    data : dict
        The data to use in the model.
    count : int, optional
        The total count of items in the API.
    name : str, optional
        The name of the API.

    ..
        TODO: Add an example of how to create the object
    """
    pass


class NGAs(BaseModel):
    """
    A class representing a single NGA (Natural Geographic Area) object in the
    Seshat API.

    Parameters
    ----------
    data : dict
        The data to use in the model.
    count : int, optional
        The total count of items in the API.
    name : str, optional
        The name of the API.

    ..
        TODO: Add an example of how to create the object
    """
    pass


class Capitals(BaseModel):
    """
    A class representing a single Capital object in the Seshat API.

    Parameters
    ----------
    data : dict
        The data to use in the model.
    count : int, optional
        The total count of items in the API.
    name : str, optional
        The name of the API.

    ..
        TODO: Add an example of how to create the object
    """
    pass


class NGAPolityRelations(BaseModel):
    """
    A class representing a single NGA–polity relation (relations between a
    Natural Geographic Area, NGA, and a polity) object in the Seshat API.

    Parameters
    ----------
    data : dict
        The data to use in the model.
    count : int, optional
        The total count of items in the API.
    name : str, optional
        The name of the API.

    ..
        TODO: Add an example of how to create the object
    """
    pass


class Countries(BaseModel):
    """
    A class representing a single Country object in the Seshat API.

    Parameters
    ----------
    data : dict
        The data to use in the model.
    count : int, optional
        The total count of items in the API.
    name : str, optional
        The name of the API.

    ..
        TODO: Add an example of how to create the object
    """
    pass


class Sections(BaseModel):
    """
    A class representing a single Section object in the Seshat API.

    Parameters
    ----------
    data : dict
        The data to use in the model.
    count : int, optional
        The total count of items in the API.
    name : str, optional
        The name of the API.

    ..
        TODO: Add an example of how to create the object
    """
    pass


class Subsections(BaseModel):
    """
    A class representing a single Subsection object in the Seshat API.

    Parameters
    ----------
    data : dict
        The data to use in the model.
    count : int, optional
        The total count of items in the API.
    name : str, optional
        The name of the API.

    ..
        TODO: Add an example of how to create the object
    """
    pass


class VariableHierarchies(BaseModel):
    """
    A class representing a single Variable Hierarchy object in the Seshat API.

    Parameters
    ----------
    data : dict
        The data to use in the model.
    count : int, optional
        The total count of items in the API.
    name : str, optional
        The name of the API.

    ..
        TODO: Add an example of how to create the object
    """
    pass


class References(BaseModel):
    """
    A class representing a single Reference object in the Seshat API.

    Parameters
    ----------
    data : dict
        The data to use in the model.
    count : int, optional
        The total count of items in the API.
    name : str, optional
        The name of the API.

    ..
        TODO: Add an example of how to create the object
    """
    pass


class Citations(BaseModel):
    """
    A class representing a single Citation object in the Seshat API.

    Parameters
    ----------
    data : dict
        The data to use in the model.
    count : int, optional
        The total count of items in the API.
    name : str, optional
        The name of the API.

    ..
        TODO: Add an example of how to create the object
    """
    pass


class Religions(BaseModel):
    """
    A class representing a single Religion object in the Seshat API.

    Parameters
    ----------
    data : dict
        The data to use in the model.
    count : int, optional
        The total count of items in the API.
    name : str, optional
        The name of the API.

    ..
        TODO: Add an example of how to create the object
    """
    pass


class CliopatriaShapefiles(BaseModel):
    """
    A class representing a single Cliopatria Shapefile object in the Seshat API.

    Parameters
    ----------
    data : dict
        The data to use in the model.
    count : int, optional
        The total count of items in the API.
    name : str, optional
        The name of the API.

    ..
        TODO: Add an example of how to create the object
    """
    pass


class GADMShapefiles(BaseModel):
    """
    A class representing a single GADM Shapefile object in the Seshat API.

    Parameters
    ----------
    data : dict
        The data to use in the model.
    count : int, optional
        The total count of items in the API.
    name : str, optional
        The name of the API.

    ..
        TODO: Add an example of how to create the object
    """
    pass


class GADMCountries(BaseModel):
    """
    A class representing a single GADM Country object in the Seshat API.

    Parameters
    ----------
    data : dict
        The data to use in the model.
    count : int, optional
        The total count of items in the API.
    name : str, optional
        The name of the API.

    ..
        TODO: Add an example of how to create the object
    """
    pass


class GADMProvinces(BaseModel):
    """
    A class representing a single GADM Province object in the Seshat API.

    Parameters
    ----------
    data : dict
        The data to use in the model.
    count : int, optional
        The total count of items in the API.
    name : str, optional
        The name of the API.

    ..
        TODO: Add an example of how to create the object
    """
    pass
