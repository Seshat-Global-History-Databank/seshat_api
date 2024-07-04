from ..base_model import BaseAPICall

from ..models import (
    WidespreadReligion,
    OfficialReligion,
    ElitesReligion,
    TheologicalSyncretismOfDifferentReligion,
    SyncretismOfReligiousPracticesAtTheLevelOfIndividualBeliever,
    ReligiousFragmentation,
    FrequencyOfGovernmentalViolenceAgainstReligiousGroup,
    GovernmentRestrictionsOnPublicWorship,
    GovernmentRestrictionsOnPublicProselytizing,
    GovernmentRestrictionsOnConversion,
    GovernmentPressureToConvert,
    GovernmentRestrictionsOnPropertyOwnershipForAdherentsOfAndReligiousGroup,
    TaxesBasedOnReligiousAdherenceOrOnReligiousActivityAndInstitution,
    GovernmentalObligationsForReligiousGroupToApplyForOfficialRecognition,
    GovernmentRestrictionsOnConstructionOfReligiousBuilding,
    GovernmentRestrictionsOnReligiousEducation,
    GovernmentRestrictionsOnCirculationOfReligiousLiterature,
    GovernmentDiscriminationAgainstReligiousGroupTakingUpCertainOccupationOrFunction,  # noqa
    FrequencyOfSocietalViolenceAgainstReligiousGroup,
    SocietalDiscriminationAgainstReligiousGroupTakingUpCertainOccupationOrFunction,  # noqa
    SocietalPressureToConvertOrAgainstConversion,
)

__all__ = [
    "WidespreadReligions",
    "OfficialReligions",
    "ElitesReligions",
    "TheologicalSyncretismOfDifferentReligions",
    "SyncretismOfReligiousPracticesAtTheLevelOfIndividualBelievers",
    "ReligiousFragmentations",
    "FrequencyOfGovernmentalViolenceAgainstReligiousGroups",
    "GovernmentRestrictionsOnPublicWorships",
    "GovernmentRestrictionsOnPublicProselytizings",
    "GovernmentRestrictionsOnConversions",
    "GovernmentPressureToConverts",
    "GovernmentRestrictionsOnPropertyOwnershipForAdherentsOfAndReligiousGroups",
    "TaxesBasedOnReligiousAdherenceOrOnReligiousActivitiesAndInstitutions",
    "GovernmentalObligationsForReligiousGroupsToApplyForOfficialRecognitions",
    "GovernmentRestrictionsOnConstructionOfReligiousBuildings",
    "GovernmentRestrictionsOnReligiousEducations",
    "GovernmentRestrictionsOnCirculationOfReligiousLiteratures",
    "GovernmentDiscriminationAgainstReligiousGroupsTakingUpCertainOccupationsOrFunctions",  # noqa
    "FrequencyOfSocietalViolenceAgainstReligiousGroups",
    "SocietalDiscriminationAgainstReligiousGroupsTakingUpCertainOccupationsOrFunctions",  # noqa
    "SocietalPressureToConvertOrAgainstConversions",
]


class WidespreadReligions(BaseAPICall):
    """
    A class for interacting with the widespread religions endpoint of the
    Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.rt import WidespreadReligions
    >>> client = SeshatAPI()
    >>> widespread_religions = WidespreadReligions(client)
    """
    ENDPOINT = "/rt/widespread-religions"
    SINGLE_MODEL = WidespreadReligion


class OfficialReligions(BaseAPICall):
    """
    A class for interacting with the official religions endpoint of the Seshat
    API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.rt import OfficialReligions
    >>> client = SeshatAPI()
    >>> official_religions = OfficialReligions(client)
    """
    ENDPOINT = "/rt/official-religions"
    SINGLE_MODEL = OfficialReligion


class ElitesReligions(BaseAPICall):
    """
    A class for interacting with the elites religions endpoint of the Seshat
    API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.rt import ElitesReligions
    >>> client = SeshatAPI()
    >>> elites_religions = ElitesReligions(client)
    """
    ENDPOINT = "/rt/elites-religions"
    SINGLE_MODEL = ElitesReligion


class TheologicalSyncretismOfDifferentReligions(BaseAPICall):
    """
    A class for interacting with the theological syncretism of different
    religions endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.rt import TheologicalSyncretismOfDifferentReligions
    >>> client = SeshatAPI()
    >>> theological_syncretism_of_different_religions = TheologicalSyncretismOfDifferentReligions(client)
    """
    ENDPOINT = "/rt/theological-syncretism-of-different-religions"
    SINGLE_MODEL = TheologicalSyncretismOfDifferentReligion


class SyncretismOfReligiousPracticesAtTheLevelOfIndividualBelievers(
    BaseAPICall
):
    ENDPOINT = "/rt/syncretism-of-religious-practices-at-the-level-of-individual-believers"  # noqa
    SINGLE_MODEL = SyncretismOfReligiousPracticesAtTheLevelOfIndividualBeliever


class ReligiousFragmentations(BaseAPICall):
    """
    A class for interacting with the religious fragmentations endpoint of the
    Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.rt import ReligiousFragmentations
    >>> client = SeshatAPI()
    >>> religious_fragmentations = ReligiousFragmentations(client)
    """
    ENDPOINT = "/rt/religious-fragmentations"
    SINGLE_MODEL = ReligiousFragmentation


class FrequencyOfGovernmentalViolenceAgainstReligiousGroups(BaseAPICall):
    """
    A class for interacting with the frequency of governmental violence against
    religious groups endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.rt import FrequencyOfGovernmentalViolenceAgainstReligiousGroups
    >>> client = SeshatAPI()
    >>> frequency_of_governmental_violence_against_religious_groups = FrequencyOfGovernmentalViolenceAgainstReligiousGroups(client)
    """
    ENDPOINT = (
        "/rt/frequency-of-governmental-violence-against-religious-groups"
    )
    SINGLE_MODEL = FrequencyOfGovernmentalViolenceAgainstReligiousGroup


class GovernmentRestrictionsOnPublicWorships(BaseAPICall):
    """
    A class for interacting with the government restrictions on public worships
    endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.rt import GovernmentRestrictionsOnPublicWorships
    >>> client = SeshatAPI()
    >>> government_restrictions_on_public_worships = GovernmentRestrictionsOnPublicWorships(client)
    """
    ENDPOINT = "/rt/government-restrictions-on-public-worships"
    SINGLE_MODEL = GovernmentRestrictionsOnPublicWorship


class GovernmentRestrictionsOnPublicProselytizings(BaseAPICall):
    """
    A class for interacting with the government restrictions on public
    proselytizings endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.rt import GovernmentRestrictionsOnPublicProselytizings
    >>> client = SeshatAPI()
    >>> government_restrictions_on_public_proselytizings = GovernmentRestrictionsOnPublicProselytizings(client)
    """
    ENDPOINT = "/rt/government-restrictions-on-public-proselytizings"
    SINGLE_MODEL = GovernmentRestrictionsOnPublicProselytizing


class GovernmentRestrictionsOnConversions(BaseAPICall):
    """
    A class for interacting with the government restrictions on conversions
    endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.rt import GovernmentRestrictionsOnConversions
    >>> client = SeshatAPI()
    >>> government_restrictions_on_conversions = GovernmentRestrictionsOnConversions(client)
    """
    ENDPOINT = "/rt/government-restrictions-on-conversions"
    SINGLE_MODEL = GovernmentRestrictionsOnConversion


class GovernmentPressureToConverts(BaseAPICall):
    """
    A class for interacting with the government pressure to converts endpoint
    of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.rt import GovernmentPressureToConverts
    >>> client = SeshatAPI()
    >>> government_pressure_to_converts = GovernmentPressureToConverts(client)
    """
    ENDPOINT = "/rt/government-pressure-to-converts"
    SINGLE_MODEL = GovernmentPressureToConvert


class GovernmentRestrictionsOnPropertyOwnershipForAdherentsOfAndReligiousGroups(  # noqa
    BaseAPICall
):
    ENDPOINT = "/rt/government-restrictions-on-property-ownership-for-adherents-of-and-religious-groups"
    SINGLE_MODEL = GovernmentRestrictionsOnPropertyOwnershipForAdherentsOfAndReligiousGroup  # noqa


class TaxesBasedOnReligiousAdherenceOrOnReligiousActivitiesAndInstitutions(
    BaseAPICall
):
    ENDPOINT = "/rt/taxes-based-on-religious-adherence-or-on-religious-activities-and-institutions"  # noqa
    SINGLE_MODEL = (
        TaxesBasedOnReligiousAdherenceOrOnReligiousActivityAndInstitution
    )


class GovernmentalObligationsForReligiousGroupsToApplyForOfficialRecognitions(
    BaseAPICall
):
    ENDPOINT = "/rt/governmental-obligations-for-religious-groups-to-apply-for-official-recognitions"  # noqa
    SINGLE_MODEL = (
        GovernmentalObligationsForReligiousGroupToApplyForOfficialRecognition
    )


class GovernmentRestrictionsOnConstructionOfReligiousBuildings(BaseAPICall):
    """
    A class for interacting with the government restrictions on construction of
    religious buildings endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.rt import GovernmentRestrictionsOnConstructionOfReligiousBuildings
    >>> client = SeshatAPI()
    >>> government_restrictions_on_construction_of_religious_buildings = GovernmentRestrictionsOnConstructionOfReligiousBuildings(client)
    """
    ENDPOINT = (
        "/rt/government-restrictions-on-construction-of-religious-buildings"
    )
    SINGLE_MODEL = GovernmentRestrictionsOnConstructionOfReligiousBuilding


class GovernmentRestrictionsOnReligiousEducations(BaseAPICall):
    """
    A class for interacting with the government restrictions on religious
    educations endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.rt import GovernmentRestrictionsOnReligiousEducations
    >>> client = SeshatAPI()
    >>> government_restrictions_on_religious_educations = GovernmentRestrictionsOnReligiousEducations(client)
    """
    ENDPOINT = "/rt/government-restrictions-on-religious-educations"
    SINGLE_MODEL = GovernmentRestrictionsOnReligiousEducation


class GovernmentRestrictionsOnCirculationOfReligiousLiteratures(BaseAPICall):
    """
    A class for interacting with the government restrictions on circulation of
    religious literatures endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.rt import GovernmentRestrictionsOnCirculationOfReligiousLiteratures
    >>> client = SeshatAPI()
    >>> government_restrictions_on_circulation_of_religious_literatures = GovernmentRestrictionsOnCirculationOfReligiousLiteratures(client)
    """
    ENDPOINT = (
        "/rt/government-restrictions-on-circulation-of-religious-literatures"
    )
    SINGLE_MODEL = GovernmentRestrictionsOnCirculationOfReligiousLiterature


class GovernmentDiscriminationAgainstReligiousGroupsTakingUpCertainOccupationsOrFunctions(  # noqa
    BaseAPICall
):
    ENDPOINT = "/rt/government-discrimination-against-religious-groups-taking-up-certain-occupations-or-functions"
    SINGLE_MODEL = GovernmentDiscriminationAgainstReligiousGroupTakingUpCertainOccupationOrFunction  # noqa


class FrequencyOfSocietalViolenceAgainstReligiousGroups(BaseAPICall):
    """
    A class for interacting with the frequency of societal violence against
    religious groups endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.rt import FrequencyOfSocietalViolenceAgainstReligiousGroups
    >>> client = SeshatAPI()
    >>> frequency_of_societal_violence_against_religious_groups = FrequencyOfSocietalViolenceAgainstReligiousGroups(client)
    """
    ENDPOINT = "/rt/frequency-of-societal-violence-against-religious-groups"
    SINGLE_MODEL = FrequencyOfSocietalViolenceAgainstReligiousGroup


class SocietalDiscriminationAgainstReligiousGroupsTakingUpCertainOccupationsOrFunctions(  # noqa
    BaseAPICall
):
    ENDPOINT = "/rt/societal-discrimination-against-religious-groups-taking-up-certain-occupations-or-functions"  # noqa
    SINGLE_MODEL = SocietalDiscriminationAgainstReligiousGroupTakingUpCertainOccupationOrFunction  # noqa


class SocietalPressureToConvertOrAgainstConversions(BaseAPICall):
    """
    A class for interacting with the societal pressure to convert or against
    conversions endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.rt import SocietalPressureToConvertOrAgainstConversions
    >>> client = SeshatAPI()
    >>> societal_pressure_to_convert_or_against_conversions = SocietalPressureToConvertOrAgainstConversions(client)
    """
    ENDPOINT = "/rt/societal-pressure-to-convert-or-against-conversions"
    SINGLE_MODEL = SocietalPressureToConvertOrAgainstConversion
