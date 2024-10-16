from ..base_model import BaseAPICall

from ..models import (
    PolityOriginalNames,
    PolityAlternativeNames,
    PolityDurations,
    PolityPeakYears,
    PolityDegreeOfCentralizations,
    PolitySuprapolities,
    PolityUTMTimezones,
    PolityCapitals,
    PolityLanguages,
    PolityLinguisticFamilies,
    PolityLanguageGenuses,
    PolityReligionGenuses,
    PolityReligionFamilies,
    PolityReligions,
    PolityRelationshipToPrecedingEntities,
    PolityPrecedingEntities,
    PolitySucceedingEntities,
    PolitySupraculturalEntities,
    PolityScaleOfSupraculturalInteractions,
    PolityAlternateReligionGenuses,
    PolityAlternateReligionFamilies,
    PolityAlternateReligions,
    PolityReligiousTraditions,
)

__all__ = [
    "PolityOriginalNames",
    "PolityAlternativeNames",
    "PolityDurations",
    "PolityPeakYears",
    "PolityDegreeOfCentralizations",
    "PolitySuprapolities",
    "PolityUTMTimezones",
    "PolityCapitals",
    "PolityLanguages",
    "PolityLinguisticFamilies",
    "PolityLanguageGenuses",
    "PolityReligionGenuses",
    "PolityReligionFamilies",
    "PolityReligions",
    "PolityRelationshipToPrecedingEntities",
    "PolityPrecedingEntities",
    "PolitySucceedingEntities",
    "PolitySupraculturalEntities",
    "PolityScaleOfSupraculturalInteractions",
    "PolityAlternateReligionGenuses",
    "PolityAlternateReligionFamilies",
    "PolityAlternateReligions",
    "PolityReligiousTraditions",
]

class PolityOriginalNames(BaseAPICall):
    """
    A class for interacting with the polity original names endpoint of the
    Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.general import PolityOriginalNames
    >>> client = SeshatAPI()
    >>> polity_original_names = PolityOriginalNames(client)
    """
    ENDPOINT = "/general/polity-original-names"
    SINGLE_MODEL = PolityOriginalNames


class PolityAlternativeNames(BaseAPICall):
    """
    A class for interacting with the polity alternative names endpoint of the
    Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.general import PolityAlternativeNames
    >>> client = SeshatAPI()
    >>> polity_alternative_names = PolityAlternativeNames(client)
    """
    ENDPOINT = "/general/polity-alternative-names"
    SINGLE_MODEL = PolityAlternativeNames


class PolityDurations(BaseAPICall):
    """
    A class for interacting with the polity durations endpoint of the Seshat
    API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.general import PolityDurations
    >>> client = SeshatAPI()
    >>> polity_durations = PolityDurations(client)
    """
    ENDPOINT = "/general/polity-durations"
    SINGLE_MODEL = PolityDurations


class PolityPeakYears(BaseAPICall):
    """
    A class for interacting with the polity peak years endpoint of the Seshat
    API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.general import PolityPeakYears
    >>> client = SeshatAPI()
    >>> polity_peak_years = PolityPeakYears(client)
    """
    ENDPOINT = "/general/polity-peak-years"
    SINGLE_MODEL = PolityPeakYears


class PolityDegreeOfCentralizations(BaseAPICall):
    """
    A class for interacting with the polity degree of centralizations endpoint
    of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.general import PolityDegreeOfCentralizations
    >>> client = SeshatAPI()
    >>> polity_degree_of_centralizations = PolityDegreeOfCentralizations(client)
    """
    ENDPOINT = "/general/polity-degree-of-centralizations"
    SINGLE_MODEL = PolityDegreeOfCentralizations


class PolitySuprapolities(BaseAPICall):
    """
    A class for interacting with the polity suprapolities endpoint of the
    Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.general import PolitySuprapolities
    >>> client = SeshatAPI()
    >>> polity_suprapolities = PolitySuprapolities(client)
    """
    ENDPOINT = "/general/polity-suprapolities"
    SINGLE_MODEL = PolitySuprapolities


class PolityUTMTimezones(BaseAPICall):
    """
    A class for interacting with the polity UTM timezones endpoint of the
    Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.general import PolityUTMTimezones
    >>> client = SeshatAPI()
    >>> polity_utm_timezones = PolityUTMTimezones(client)
    """
    ENDPOINT = "/general/polity-utm-timezones"
    SINGLE_MODEL = PolityUTMTimezones


class PolityCapitals(BaseAPICall):
    """
    A class for interacting with the polity capitals endpoint of the Seshat
    API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.general import PolityCapitals
    >>> client = SeshatAPI()
    >>> polity_capitals = PolityCapitals(client)
    """
    ENDPOINT = "/general/polity-capitals"
    SINGLE_MODEL = PolityCapitals


class PolityLanguages(BaseAPICall):
    """
    A class for interacting with the polity languages endpoint of the Seshat
    API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.general import PolityLanguages
    >>> client = SeshatAPI()
    >>> polity_languages = PolityLanguages(client)
    """
    ENDPOINT = "/general/polity-languages"
    SINGLE_MODEL = PolityLanguages


class PolityLinguisticFamilies(BaseAPICall):
    """
    A class for interacting with the polity linguistic families endpoint of the
    Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.general import PolityLinguisticFamilies
    >>> client = SeshatAPI()
    >>> polity_linguistic_families = PolityLinguisticFamilies(client)
    """
    ENDPOINT = "/general/polity-linguistic-families"
    SINGLE_MODEL = PolityLinguisticFamilies


class PolityLanguageGenuses(BaseAPICall):
    """
    A class for interacting with the polity language genuses endpoint of the
    Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.general import PolityLanguageGenuses
    >>> client = SeshatAPI()
    >>> polity_language_genuses = PolityLanguageGenuses(client)
    """
    ENDPOINT = "/general/polity-language-genuses"
    SINGLE_MODEL = PolityLanguageGenuses


class PolityReligionGenuses(BaseAPICall):
    """
    A class for interacting with the polity religion genuses endpoint of the
    Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.general import PolityReligionGenuses
    >>> client = SeshatAPI()
    >>> polity_religion_genuses = PolityReligionGenuses(client)
    """
    ENDPOINT = "/general/polity-religion-genuses"
    SINGLE_MODEL = PolityReligionGenuses


class PolityReligionFamilies(BaseAPICall):
    """
    A class for interacting with the polity religion families endpoint of the
    Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.general import PolityReligionFamilies
    >>> client = SeshatAPI()
    >>> polity_religion_families = PolityReligionFamilies(client)
    """
    ENDPOINT = "/general/polity-religion-families"
    SINGLE_MODEL = PolityReligionFamilies


class PolityReligions(BaseAPICall):
    """
    A class for interacting with the polity religions endpoint of the Seshat
    API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.general import PolityReligions
    >>> client = SeshatAPI()
    >>> polity_religions = PolityReligions(client)
    """
    ENDPOINT = "/general/polity-religions"
    SINGLE_MODEL = PolityReligions


class PolityRelationshipToPrecedingEntities(BaseAPICall):
    """
    A class for interacting with the polity relationship to preceding entities
    endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.general import PolityRelationshipToPrecedingEntities
    >>> client = SeshatAPI()
    >>> polity_relationship_to_preceding_entities = PolityRelationshipToPrecedingEntities(client)
    """
    ENDPOINT = "/general/polity-relationship-to-preceding-entities"
    SINGLE_MODEL = PolityRelationshipToPrecedingEntities


class PolityPrecedingEntities(BaseAPICall):
    """
    A class for interacting with the polity preceding entities endpoint of the
    Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.general import PolityPrecedingEntities
    >>> client = SeshatAPI()
    >>> polity_preceding_entities = PolityPrecedingEntities(client)
    """
    ENDPOINT = "/general/polity-preceding-entities"
    SINGLE_MODEL = PolityPrecedingEntities


class PolitySucceedingEntities(BaseAPICall):
    """
    A class for interacting with the polity succeeding entities endpoint of the
    Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.general import PolitySucceedingEntities
    >>> client = SeshatAPI()
    >>> polity_succeeding_entities = PolitySucceedingEntities(client)
    """
    ENDPOINT = "/general/polity-succeeding-entities"
    SINGLE_MODEL = PolitySucceedingEntities


class PolitySupraculturalEntities(BaseAPICall):
    """
    A class for interacting with the polity supracultural entities endpoint of
    the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.general import PolitySupraculturalEntities
    >>> client = SeshatAPI()
    >>> polity_supracultural_entities = PolitySupraculturalEntities(client)
    """
    ENDPOINT = "/general/polity-supracultural-entities"
    SINGLE_MODEL = PolitySupraculturalEntities


class PolityScaleOfSupraculturalInteractions(BaseAPICall):
    """
    A class for interacting with the polity scale of supracultural interactions
    endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.general import PolityScaleOfSupraculturalInteractions
    >>> client = SeshatAPI()
    >>> polity_scale_of_supracultural_interactions = PolityScaleOfSupraculturalInteractions(client)
    """
    ENDPOINT = "/general/polity-scale-of-supracultural-interactions"
    SINGLE_MODEL = PolityScaleOfSupraculturalInteractions


class PolityAlternateReligionGenuses(BaseAPICall):
    """
    A class for interacting with the polity alternate religion genuses endpoint
    of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.general import PolityAlternateReligionGenuses
    >>> client = SeshatAPI()
    >>> polity_alternate_religion_genuses = PolityAlternateReligionGenuses(client)
    """
    ENDPOINT = "/general/polity-alternate-religion-genuses"
    SINGLE_MODEL = PolityAlternateReligionGenuses


class PolityAlternateReligionFamilies(BaseAPICall):
    """
    A class for interacting with the polity alternate religion families
    endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.general import PolityAlternateReligionFamilies
    >>> client = SeshatAPI()
    >>> polity_alternate_religion_families = PolityAlternateReligionFamilies(client)
    """
    ENDPOINT = "/general/polity-alternate-religion-families"
    SINGLE_MODEL = PolityAlternateReligionFamilies


class PolityAlternateReligions(BaseAPICall):
    """
    A class for interacting with the polity alternate religions endpoint of the
    Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.general import PolityAlternateReligions
    >>> client = SeshatAPI()
    >>> polity_alternate_religions = PolityAlternateReligions(client)
    """
    ENDPOINT = "/general/polity-alternate-religions"
    SINGLE_MODEL = PolityAlternateReligions


class PolityReligiousTraditions(BaseAPICall):
    """
    A class for interacting with the polity religious traditions endpoint of
    the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.general import PolityReligiousTraditions
    >>> client = SeshatAPI()
    >>> polity_religious_traditions = PolityReligiousTraditions(client)
    """
    ENDPOINT = "/general/polity-religious-traditions"
    SINGLE_MODEL = PolityReligiousTraditions
