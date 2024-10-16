from ..base_model import BaseAPICall

from ..models import (
    PolityTerritories,
    PolityPopulations,
    PopulationOfTheLargestSettlements,
    SettlementHierarchies,
    AdministrativeLevels,
    ReligiousLevels,
    MilitaryLevels,
    ProfessionalMilitaryOfficers,
    ProfessionalSoldiers,
    ProfessionalPriesthoods,
    FullTimeBureaucrats,
    ExaminationSystems,
    MeritPromotions,
    SpecializedGovernmentBuildings,
    FormalLegalCodes,
    Judges,
    Courts,
    ProfessionalLawyers,
    IrrigationSystems,
    DrinkingWaterSupplies,
    Markets,
    FoodStorageSites,
    Roads,
    Bridges,
    Canals,
    Ports,
    MinesOrQuarries,
    MnemonicDevices,
    NonwrittenRecords,
    WrittenRecords,
    Scripts,
    NonPhoneticWritings,
    PhoneticAlphabeticWritings,
    ListsTablesAndClassifications,
    Calendars,
    SacredTexts,
    ReligiousLiteratures,
    PracticalLiteratures,
    Histories,
    Philosophies,
    ScientificLiteratures,
    Fictions,
    Articles,
    Tokens,
    PreciousMetals,
    ForeignCoins,
    IndigenousCoins,
    PaperCurrencies,
    Couriers,
    PostalStations,
    GeneralPostalServices,
    CommunalBuildings,
    UtilitarianPublicBuildings,
    SymbolicBuildings,
    EntertainmentBuildings,
    KnowledgeOrInformationBuildings,
    OtherUtilitarianPublicBuildings,
    SpecialPurposeSites,
    CeremonialSites,
    BurialSites,
    TradingEmporia,
    Enclosures,
    LengthMeasurementSystems,
    AreaMeasurementSystems,
    VolumeMeasurementSystems,
    WeightMeasurementSystems,
    TimeMeasurementSystems,
    GeometricalMeasurementSystems,
    OtherMeasurementSystems,
    DebtAndCreditStructures,
    StoresOfWealth,
    SourcesOfSupport,
    OccupationalComplexities,
    SpecialPurposeHouses,
    OtherSpecialPurposeSites,
    LargestCommunicationDistances,
    FastestIndividualCommunications,
)

__all__ = [
    "PolityTerritories",
    "PolityPopulations",
    "PopulationOfTheLargestSettlements",
    "SettlementHierarchies",
    "AdministrativeLevels",
    "ReligiousLevels",
    "MilitaryLevels",
    "ProfessionalMilitaryOfficers",
    "ProfessionalSoldiers",
    "ProfessionalPriesthoods",
    "FullTimeBureaucrats",
    "ExaminationSystems",
    "MeritPromotions",
    "SpecializedGovernmentBuildings",
    "FormalLegalCodes",
    "Judges",
    "Courts",
    "ProfessionalLawyers",
    "IrrigationSystems",
    "DrinkingWaterSupplies",
    "Markets",
    "FoodStorageSites",
    "Roads",
    "Bridges",
    "Canals",
    "Ports",
    "MinesOrQuarries",
    "MnemonicDevices",
    "NonwrittenRecords",
    "WrittenRecords",
    "Scripts",
    "NonPhoneticWritings",
    "PhoneticAlphabeticWritings",
    "ListsTablesAndClassifications",
    "Calendars",
    "SacredTexts",
    "ReligiousLiteratures",
    "PracticalLiteratures",
    "Histories",
    "Philosophies",
    "ScientificLiteratures",
    "Fictions",
    "Articles",
    "Tokens",
    "PreciousMetals",
    "ForeignCoins",
    "IndigenousCoins",
    "PaperCurrencies",
    "Couriers",
    "PostalStations",
    "GeneralPostalServices",
    "CommunalBuildings",
    "UtilitarianPublicBuildings",
    "SymbolicBuildings",
    "EntertainmentBuildings",
    "KnowledgeOrInformationBuildings",
    "OtherUtilitarianPublicBuildings",
    "SpecialPurposeSites",
    "CeremonialSites",
    "BurialSites",
    "TradingEmporia",
    "Enclosures",
    "LengthMeasurementSystems",
    "AreaMeasurementSystems",
    "VolumeMeasurementSystems",
    "WeightMeasurementSystems",
    "TimeMeasurementSystems",
    "GeometricalMeasurementSystems",
    "OtherMeasurementSystems",
    "DebtAndCreditStructures",
    "StoresOfWealth",
    "SourcesOfSupport",
    "OccupationalComplexities",
    "SpecialPurposeHouses",
    "OtherSpecialPurposeSites",
    "LargestCommunicationDistances",
    "FastestIndividualCommunications",
]


class PolityTerritories(BaseAPICall):
    """
    A class for interacting with the polity territories endpoint of the Seshat
    API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import PolityTerritories
    >>> client = SeshatAPI()
    >>> polity_territories = PolityTerritories(client)
    """
    ENDPOINT = "/sc/polity-territories"
    SINGLE_MODEL = PolityTerritories


class PolityPopulations(BaseAPICall):
    """
    A class for interacting with the polity populations endpoint of the Seshat
    API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import PolityPopulations
    >>> client = SeshatAPI()
    >>> polity_populations = PolityPopulations(client)
    """
    ENDPOINT = "/sc/polity-populations"
    SINGLE_MODEL = PolityPopulations


class PopulationOfTheLargestSettlements(BaseAPICall):
    """
    A class for interacting with the population of the largest settlements
    endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import PopulationOfTheLargestSettlements
    >>> client = SeshatAPI()
    >>> population_of_the_largest_settlements = PopulationOfTheLargestSettlements(client)
    """
    ENDPOINT = "/sc/population-of-the-largest-settlements"
    SINGLE_MODEL = PopulationOfTheLargestSettlements


class SettlementHierarchies(BaseAPICall):
    """
    A class for interacting with the settlement hierarchies endpoint of the
    Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import SettlementHierarchies
    >>> client = SeshatAPI()
    >>> settlement_hierarchies = SettlementHierarchies(client)
    """
    ENDPOINT = "/sc/settlement-hierarchies"
    SINGLE_MODEL = SettlementHierarchies


class AdministrativeLevels(BaseAPICall):
    """
    A class for interacting with the administrative levels endpoint of the
    Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import AdministrativeLevels
    >>> client = SeshatAPI()
    >>> administrative_levels = AdministrativeLevels(client)
    """
    ENDPOINT = "/sc/administrative-levels"
    SINGLE_MODEL = AdministrativeLevels


class ReligiousLevels(BaseAPICall):
    """
    A class for interacting with the religious levels endpoint of the Seshat
    API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import ReligiousLevels
    >>> client = SeshatAPI()
    >>> religious_levels = ReligiousLevels(client)
    """
    ENDPOINT = "/sc/religious-levels"
    SINGLE_MODEL = ReligiousLevels


class MilitaryLevels(BaseAPICall):
    """
    A class for interacting with the military levels endpoint of the Seshat
    API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import MilitaryLevels
    >>> client = SeshatAPI()
    >>> military_levels = MilitaryLevels(client)
    """
    ENDPOINT = "/sc/military-levels"
    SINGLE_MODEL = MilitaryLevels


class ProfessionalMilitaryOfficers(BaseAPICall):
    """
    A class for interacting with the professional military officers endpoint of
    the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import ProfessionalMilitaryOfficers
    >>> client = SeshatAPI()
    >>> professional_military_officers = ProfessionalMilitaryOfficers(client)
    """
    ENDPOINT = "/sc/professional-military-officers"
    SINGLE_MODEL = ProfessionalMilitaryOfficers


class ProfessionalSoldiers(BaseAPICall):
    """
    A class for interacting with the professional soldiers endpoint of the
    Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import ProfessionalSoldiers
    >>> client = SeshatAPI()
    >>> professional_soldiers = ProfessionalSoldiers(client)
    """
    ENDPOINT = "/sc/professional-soldiers"
    SINGLE_MODEL = ProfessionalSoldiers


class ProfessionalPriesthoods(BaseAPICall):
    """
    A class for interacting with the professional priesthoods endpoint of the
    Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import ProfessionalPriesthoods
    >>> client = SeshatAPI()
    >>> professional_priesthoods = ProfessionalPriesthoods(client)
    """
    ENDPOINT = "/sc/professional-priesthoods"
    SINGLE_MODEL = ProfessionalPriesthoods


class FullTimeBureaucrats(BaseAPICall):
    """
    A class for interacting with the full-time bureaucrats endpoint of the
    Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import FullTimeBureaucrats
    >>> client = SeshatAPI()
    >>> full_time_bureaucrats = FullTimeBureaucrats(client)
    """
    ENDPOINT = "/sc/full-time-bureaucrats"
    SINGLE_MODEL = FullTimeBureaucrats


class ExaminationSystems(BaseAPICall):
    """
    A class for interacting with the examination systems endpoint of the Seshat
    API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import ExaminationSystems
    >>> client = SeshatAPI()
    >>> examination_systems = ExaminationSystems(client)
    """
    ENDPOINT = "/sc/examination-systems"
    SINGLE_MODEL = ExaminationSystems


class MeritPromotions(BaseAPICall):
    """
    A class for interacting with the merit promotions endpoint of the Seshat
    API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import MeritPromotions
    >>> client = SeshatAPI()
    >>> merit_promotions = MeritPromotions(client)
    """
    ENDPOINT = "/sc/merit-promotions"
    SINGLE_MODEL = MeritPromotions


class SpecializedGovernmentBuildings(BaseAPICall):
    """
    A class for interacting with the specialized government buildings endpoint
    of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import SpecializedGovernmentBuildings
    >>> client = SeshatAPI()
    >>> specialized_government_buildings = SpecializedGovernmentBuildings(client)
    """
    ENDPOINT = "/sc/specialized-government-buildings"
    SINGLE_MODEL = SpecializedGovernmentBuildings


class FormalLegalCodes(BaseAPICall):
    """
    A class for interacting with the formal legal codes endpoint of the Seshat
    API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import FormalLegalCodes
    >>> client = SeshatAPI()
    >>> formal_legal_codes = FormalLegalCodes(client)
    """
    ENDPOINT = "/sc/formal-legal-codes"
    SINGLE_MODEL = FormalLegalCodes


class Judges(BaseAPICall):
    """
    A class for interacting with the judges endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import Judges
    >>> client = SeshatAPI()
    >>> judges = Judges(client)
    """
    ENDPOINT = "/sc/judges"
    SINGLE_MODEL = Judges


class Courts(BaseAPICall):
    """
    A class for interacting with the courts endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import Courts
    >>> client = SeshatAPI()
    >>> courts = Courts(client)
    """
    ENDPOINT = "/sc/courts"
    SINGLE_MODEL = Courts


class ProfessionalLawyers(BaseAPICall):
    """
    A class for interacting with the professional lawyers endpoint of the
    Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import ProfessionalLawyers
    >>> client = SeshatAPI()
    >>> professional_lawyers = ProfessionalLawyers(client)
    """
    ENDPOINT = "/sc/professional-lawyers"
    SINGLE_MODEL = ProfessionalLawyers


class IrrigationSystems(BaseAPICall):
    """
    A class for interacting with the irrigation systems endpoint of the Seshat
    API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import IrrigationSystems
    >>> client = SeshatAPI()
    >>> irrigation_systems = IrrigationSystems(client)
    """
    ENDPOINT = "/sc/irrigation-systems"
    SINGLE_MODEL = IrrigationSystems


class DrinkingWaterSupplies(BaseAPICall):
    """
    A class for interacting with the drinking water supplies endpoint of the
    Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import DrinkingWaterSupplies
    >>> client = SeshatAPI()
    >>> drinking_water_supplies = DrinkingWaterSupplies(client)
    """
    ENDPOINT = "/sc/drinking-water-supplies"
    SINGLE_MODEL = DrinkingWaterSupplies


class Markets(BaseAPICall):
    """
    A class for interacting with the markets endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import Markets
    >>> client = SeshatAPI()
    >>> markets = Markets(client)
    """
    ENDPOINT = "/sc/markets"
    SINGLE_MODEL = Markets


class FoodStorageSites(BaseAPICall):
    """
    A class for interacting with the food storage sites endpoint of the Seshat
    API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import FoodStorageSites
    >>> client = SeshatAPI()
    >>> food_storage_sites = FoodStorageSites(client)
    """
    ENDPOINT = "/sc/food-storage-sites"
    SINGLE_MODEL = FoodStorageSites


class Roads(BaseAPICall):
    """
    A class for interacting with the roads endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import Roads
    >>> client = SeshatAPI()
    >>> roads = Roads(client)
    """
    ENDPOINT = "/sc/roads"
    SINGLE_MODEL = Roads


class Bridges(BaseAPICall):
    """
    A class for interacting with the bridges endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import Bridges
    >>> client = SeshatAPI()
    >>> bridges = Bridges(client)
    """
    ENDPOINT = "/sc/bridges"
    SINGLE_MODEL = Bridges


class Canals(BaseAPICall):
    """
    A class for interacting with the canals endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import Canals
    >>> client = SeshatAPI()
    >>> canals = Canals(client)
    """
    ENDPOINT = "/sc/canals"
    SINGLE_MODEL = Canals


class Ports(BaseAPICall):
    """
    A class for interacting with the ports endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import Ports
    >>> client = SeshatAPI()
    >>> ports = Ports(client)
    """
    ENDPOINT = "/sc/ports"
    SINGLE_MODEL = Ports


class MinesOrQuarries(BaseAPICall):
    """
    A class for interacting with the mines or quarries endpoint of the Seshat
    API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import MinesOrQuarries
    >>> client = SeshatAPI()
    >>> mines_or_quarries = MinesOrQuarries(client)
    """
    ENDPOINT = "/sc/mines-or-quarries"
    SINGLE_MODEL = MinesOrQuarries


class MnemonicDevices(BaseAPICall):
    """
    A class for interacting with the mnemonic devices endpoint of the Seshat
    API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import MnemonicDevices
    >>> client = SeshatAPI()
    >>> mnemonic_devices = MnemonicDevices(client)
    """
    ENDPOINT = "/sc/mnemonic-devices"
    SINGLE_MODEL = MnemonicDevices


class NonwrittenRecords(BaseAPICall):
    """
    A class for interacting with the nonwritten records endpoint of the Seshat
    API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import NonwrittenRecords
    >>> client = SeshatAPI()
    >>> nonwritten_records = NonwrittenRecords(client)
    """
    ENDPOINT = "/sc/nonwritten-records"
    SINGLE_MODEL = NonwrittenRecords


class WrittenRecords(BaseAPICall):
    """
    A class for interacting with the written records endpoint of the Seshat
    API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import WrittenRecords
    >>> client = SeshatAPI()
    >>> written_records = WrittenRecords(client)
    """
    ENDPOINT = "/sc/written-records"
    SINGLE_MODEL = WrittenRecords


class Scripts(BaseAPICall):
    """
    A class for interacting with the scripts endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import Scripts
    >>> client = SeshatAPI()
    >>> scripts = Scripts(client)
    """
    ENDPOINT = "/sc/scripts"
    SINGLE_MODEL = Scripts


class NonPhoneticWritings(BaseAPICall):
    """
    A class for interacting with the non-phonetic writings endpoint of the
    Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import NonPhoneticWritings
    >>> client = SeshatAPI()
    >>> non_phonetic_writings = NonPhoneticWritings(client)
    """
    ENDPOINT = "/sc/non-phonetic-writings"
    SINGLE_MODEL = NonPhoneticWritings


class PhoneticAlphabeticWritings(BaseAPICall):
    """
    A class for interacting with the phonetic alphabetic writings endpoint of
    the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import PhoneticAlphabeticWritings
    >>> client = SeshatAPI()
    >>> phonetic_alphabetic_writings = PhoneticAlphabeticWritings(client)
    """
    ENDPOINT = "/sc/phonetic-alphabetic-writings"
    SINGLE_MODEL = PhoneticAlphabeticWritings


class ListsTablesAndClassifications(BaseAPICall):
    """
    A class for interacting with the lists, tables, and classifications
    endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import ListsTablesAndClassifications
    >>> client = SeshatAPI()
    >>> lists_tables_and_classifications = ListsTablesAndClassifications(client)
    """
    ENDPOINT = "/sc/lists-tables-and-classifications"
    SINGLE_MODEL = ListsTablesAndClassifications


class Calendars(BaseAPICall):
    """
    A class for interacting with the calendars endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import Calendars
    >>> client = SeshatAPI()
    >>> calendars = Calendars(client)
    """
    ENDPOINT = "/sc/calendars"
    SINGLE_MODEL = Calendars


class SacredTexts(BaseAPICall):
    """
    A class for interacting with the sacred texts endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import SacredTexts
    >>> client = SeshatAPI()
    >>> sacred_texts = SacredTexts(client)
    """
    ENDPOINT = "/sc/sacred-texts"
    SINGLE_MODEL = SacredTexts


class ReligiousLiteratures(BaseAPICall):
    """
    A class for interacting with the religious literatures endpoint of the
    Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import ReligiousLiteratures
    >>> client = SeshatAPI()
    >>> religious_literatures = ReligiousLiteratures(client)
    """
    ENDPOINT = "/sc/religious-literatures"
    SINGLE_MODEL = ReligiousLiteratures


class PracticalLiteratures(BaseAPICall):
    """
    A class for interacting with the practical literatures endpoint of the
    Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import PracticalLiteratures
    >>> client = SeshatAPI()
    >>> practical_literatures = PracticalLiteratures(client)
    """
    ENDPOINT = "/sc/practical-literatures"
    SINGLE_MODEL = PracticalLiteratures


class Histories(BaseAPICall):
    """
    A class for interacting with the histories endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import Histories
    >>> client = SeshatAPI()
    >>> histories = Histories(client)
    """
    ENDPOINT = "/sc/histories"
    SINGLE_MODEL = Histories


class Philosophies(BaseAPICall):
    """
    A class for interacting with the philosophies endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import Philosophies
    >>> client = SeshatAPI()
    >>> philosophies = Philosophies(client)
    """
    ENDPOINT = "/sc/philosophies"
    SINGLE_MODEL = Philosophies


class ScientificLiteratures(BaseAPICall):
    """
    A class for interacting with the scientific literatures endpoint of the
    Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import ScientificLiteratures
    >>> client = SeshatAPI()
    >>> scientific_literatures = ScientificLiteratures(client)
    """
    ENDPOINT = "/sc/scientific-literatures"
    SINGLE_MODEL = ScientificLiteratures


class Fictions(BaseAPICall):
    """
    A class for interacting with the fictions endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import Fictions
    >>> client = SeshatAPI()
    >>> fictions = Fictions(client)
    """
    ENDPOINT = "/sc/fictions"
    SINGLE_MODEL = Fictions


class Articles(BaseAPICall):
    """
    A class for interacting with the articles endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import Articles
    >>> client = SeshatAPI()
    >>> articles = Articles(client)
    """
    ENDPOINT = "/sc/articles"
    SINGLE_MODEL = Articles


class Tokens(BaseAPICall):
    """
    A class for interacting with the tokens endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import Tokens
    >>> client = SeshatAPI()
    >>> tokens = Tokens(client)
    """
    ENDPOINT = "/sc/tokens"
    SINGLE_MODEL = Tokens


class PreciousMetals(BaseAPICall):
    """
    A class for interacting with the precious metals endpoint of the Seshat
    API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import PreciousMetals
    >>> client = SeshatAPI()
    >>> precious_metals = PreciousMetals(client)
    """
    ENDPOINT = "/sc/precious-metals"
    SINGLE_MODEL = PreciousMetals


class ForeignCoins(BaseAPICall):
    """
    A class for interacting with the foreign coins endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import ForeignCoins
    >>> client = SeshatAPI()
    >>> foreign_coins = ForeignCoins(client)
    """
    ENDPOINT = "/sc/foreign-coins"
    SINGLE_MODEL = ForeignCoins


class IndigenousCoins(BaseAPICall):
    """
    A class for interacting with the indigenous coins endpoint of the Seshat
    API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import IndigenousCoins
    >>> client = SeshatAPI()
    >>> indigenous_coins = IndigenousCoins(client)
    """
    ENDPOINT = "/sc/indigenous-coins"
    SINGLE_MODEL = IndigenousCoins


class PaperCurrencies(BaseAPICall):
    """
    A class for interacting with the paper currencies endpoint of the Seshat
    API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import PaperCurrencies
    >>> client = SeshatAPI()
    >>> paper_currencies = PaperCurrencies(client)
    """
    ENDPOINT = "/sc/paper-currencies"
    SINGLE_MODEL = PaperCurrencies


class Couriers(BaseAPICall):
    """
    A class for interacting with the couriers endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import Couriers
    >>> client = SeshatAPI()
    >>> couriers = Couriers(client)
    """
    ENDPOINT = "/sc/couriers"
    SINGLE_MODEL = Couriers


class PostalStations(BaseAPICall):
    """
    A class for interacting with the postal stations endpoint of the Seshat
    API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import PostalStations
    >>> client = SeshatAPI()
    >>> postal_stations = PostalStations(client)
    """
    ENDPOINT = "/sc/postal-stations"
    SINGLE_MODEL = PostalStations


class GeneralPostalServices(BaseAPICall):
    """
    A class for interacting with the general postal services endpoint of the
    Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import GeneralPostalServices
    >>> client = SeshatAPI()
    >>> general_postal_services = GeneralPostalServices(client)
    """
    ENDPOINT = "/sc/general-postal-services"
    SINGLE_MODEL = GeneralPostalServices


class CommunalBuildings(BaseAPICall):
    """
    A class for interacting with the communal buildings endpoint of the Seshat
    API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import CommunalBuildings
    >>> client = SeshatAPI()
    >>> communal_buildings = CommunalBuildings(client)
    """
    ENDPOINT = "/sc/communal-buildings"
    SINGLE_MODEL = CommunalBuildings


class UtilitarianPublicBuildings(BaseAPICall):
    """
    A class for interacting with the utilitarian public buildings endpoint of
    the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import UtilitarianPublicBuildings
    >>> client = SeshatAPI()
    >>> utilitarian_public_buildings = UtilitarianPublicBuildings(client)
    """
    ENDPOINT = "/sc/utilitarian-public-buildings"
    SINGLE_MODEL = UtilitarianPublicBuildings


class SymbolicBuildings(BaseAPICall):
    """
    A class for interacting with the symbolic buildings endpoint of the Seshat
    API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import SymbolicBuildings
    >>> client = SeshatAPI()
    >>> symbolic_buildings = SymbolicBuildings(client)
    """
    ENDPOINT = "/sc/symbolic-buildings"
    SINGLE_MODEL = SymbolicBuildings


class EntertainmentBuildings(BaseAPICall):
    """
    A class for interacting with the entertainment buildings endpoint of the
    Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import EntertainmentBuildings
    >>> client = SeshatAPI()
    >>> entertainment_buildings = EntertainmentBuildings(client)
    """
    ENDPOINT = "/sc/entertainment-buildings"
    SINGLE_MODEL = EntertainmentBuildings


class KnowledgeOrInformationBuildings(BaseAPICall):
    """
    A class for interacting with the knowledge or information buildings
    endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import KnowledgeOrInformationBuildings
    >>> client = SeshatAPI()
    >>> knowledge_or_information_buildings = KnowledgeOrInformationBuildings(client)
    """
    ENDPOINT = "/sc/knowledge-or-information-buildings"
    SINGLE_MODEL = KnowledgeOrInformationBuildings


class OtherUtilitarianPublicBuildings(BaseAPICall):
    """
    A class for interacting with the other utilitarian public buildings
    endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import OtherUtilitarianPublicBuildings
    >>> client = SeshatAPI()
    >>> other_utilitarian_public_buildings = OtherUtilitarianPublicBuildings(client)
    """
    ENDPOINT = "/sc/other-utilitarian-public-buildings"
    SINGLE_MODEL = OtherUtilitarianPublicBuildings


class SpecialPurposeSites(BaseAPICall):
    """
    A class for interacting with the special purpose sites endpoint of the
    Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import SpecialPurposeSites
    >>> client = SeshatAPI()
    >>> special_purpose_sites = SpecialPurposeSites(client)
    """
    ENDPOINT = "/sc/special-purpose-sites"
    SINGLE_MODEL = SpecialPurposeSites


class CeremonialSites(BaseAPICall):
    """
    A class for interacting with the ceremonial sites endpoint of the Seshat
    API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import CeremonialSites
    >>> client = SeshatAPI()
    >>> ceremonial_sites = CeremonialSites(client)
    """
    ENDPOINT = "/sc/ceremonial-sites"
    SINGLE_MODEL = CeremonialSites


class BurialSites(BaseAPICall):
    """
    A class for interacting with the burial sites endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import BurialSites
    >>> client = SeshatAPI()
    >>> burial_sites = BurialSites(client)
    """
    ENDPOINT = "/sc/burial-sites"
    SINGLE_MODEL = BurialSites


class TradingEmporia(BaseAPICall):
    """
    A class for interacting with the trading emporia endpoint of the Seshat
    API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import TradingEmporia
    >>> client = SeshatAPI()
    >>> trading_emporia = TradingEmporia(client)
    """
    ENDPOINT = "/sc/trading-emporia"
    SINGLE_MODEL = TradingEmporia


class Enclosures(BaseAPICall):
    """
    A class for interacting with the enclosures endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import Enclosures
    >>> client = SeshatAPI()
    >>> enclosures = Enclosures(client)
    """
    ENDPOINT = "/sc/enclosures"
    SINGLE_MODEL = Enclosures


class LengthMeasurementSystems(BaseAPICall):
    """
    A class for interacting with the length measurement systems endpoint of the
    Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import LengthMeasurementSystems
    >>> client = SeshatAPI()
    >>> length_measurement_systems = LengthMeasurementSystems(client)
    """
    ENDPOINT = "/sc/length-measurement-systems"
    SINGLE_MODEL = LengthMeasurementSystems


class AreaMeasurementSystems(BaseAPICall):
    """
    A class for interacting with the area measurement systems endpoint of the
    Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import AreaMeasurementSystems
    >>> client = SeshatAPI()
    >>> area_measurement_systems = AreaMeasurementSystems(client)
    """
    ENDPOINT = "/sc/area-measurement-systems"
    SINGLE_MODEL = AreaMeasurementSystems


class VolumeMeasurementSystems(BaseAPICall):
    """
    A class for interacting with the volume measurement systems endpoint of the
    Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import VolumeMeasurementSystems
    >>> client = SeshatAPI()
    >>> volume_measurement_systems = VolumeMeasurementSystems(client)
    """
    ENDPOINT = "/sc/volume-measurement-systems"
    SINGLE_MODEL = VolumeMeasurementSystems


class WeightMeasurementSystems(BaseAPICall):
    """
    A class for interacting with the weight measurement systems endpoint of the
    Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import WeightMeasurementSystems
    >>> client = SeshatAPI()
    >>> weight_measurement_systems = WeightMeasurementSystems(client)
    """
    ENDPOINT = "/sc/weight-measurement-systems"
    SINGLE_MODEL = WeightMeasurementSystems


class TimeMeasurementSystems(BaseAPICall):
    """
    A class for interacting with the time measurement systems endpoint of the
    Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import TimeMeasurementSystems
    >>> client = SeshatAPI()
    >>> time_measurement_systems = TimeMeasurementSystems(client)
    """
    ENDPOINT = "/sc/time-measurement-systems"
    SINGLE_MODEL = TimeMeasurementSystems


class GeometricalMeasurementSystems(BaseAPICall):
    """
    A class for interacting with the geometrical measurement systems endpoint
    of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import GeometricalMeasurementSystems
    >>> client = SeshatAPI()
    >>> geometrical_measurement_systems = GeometricalMeasurementSystems(client)
    """
    ENDPOINT = "/sc/geometrical-measurement-systems"
    SINGLE_MODEL = GeometricalMeasurementSystems


class OtherMeasurementSystems(BaseAPICall):
    """
    A class for interacting with the other measurement systems endpoint of the
    Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import OtherMeasurementSystems
    >>> client = SeshatAPI()
    >>> other_measurement_systems = OtherMeasurementSystems(client)
    """
    ENDPOINT = "/sc/other-measurement-systems"
    SINGLE_MODEL = OtherMeasurementSystems


class DebtAndCreditStructures(BaseAPICall):
    """
    A class for interacting with the debt and credit structures endpoint of the
    Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import DebtAndCreditStructures
    >>> client = SeshatAPI()
    >>> debt_and_credit_structures = DebtAndCreditStructures(client)
    """
    ENDPOINT = "/sc/debt-and-credit-structures"
    SINGLE_MODEL = DebtAndCreditStructures


class StoresOfWealth(BaseAPICall):
    """
    A class for interacting with the stores of wealth endpoint of the Seshat
    API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import StoresOfWealth
    >>> client = SeshatAPI()
    >>> stores_of_wealth = StoresOfWealth(client)
    """
    ENDPOINT = "/sc/stores-of-wealth"
    SINGLE_MODEL = StoresOfWealth


class SourcesOfSupport(BaseAPICall):
    """
    A class for interacting with the sources of support endpoint of the Seshat
    API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import SourcesOfSupport
    >>> client = SeshatAPI()
    >>> sources_of_support = SourcesOfSupport(client)
    """
    ENDPOINT = "/sc/sources-of-support"
    SINGLE_MODEL = SourcesOfSupport


class OccupationalComplexities(BaseAPICall):
    """
    A class for interacting with the occupational complexities endpoint of the
    Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import OccupationalComplexities
    >>> client = SeshatAPI()
    >>> occupational_complexities = OccupationalComplexities(client)
    """
    ENDPOINT = "/sc/occupational-complexities"
    SINGLE_MODEL = OccupationalComplexities


class SpecialPurposeHouses(BaseAPICall):
    """
    A class for interacting with the special purpose houses endpoint of the
    Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import SpecialPurposeHouses
    >>> client = SeshatAPI()
    >>> special_purpose_houses = SpecialPurposeHouses(client)
    """
    ENDPOINT = "/sc/special-purpose-houses"
    SINGLE_MODEL = SpecialPurposeHouses


class OtherSpecialPurposeSites(BaseAPICall):
    """
    A class for interacting with the other special purpose sites endpoint of
    the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import OtherSpecialPurposeSites
    >>> client = SeshatAPI()
    >>> other_special_purpose_sites = OtherSpecialPurposeSites(client)
    """
    ENDPOINT = "/sc/other-special-purpose-sites"
    SINGLE_MODEL = OtherSpecialPurposeSites


class LargestCommunicationDistances(BaseAPICall):
    """
    A class for interacting with the largest communication distances endpoint
    of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import LargestCommunicationDistances
    >>> client = SeshatAPI()
    >>> largest_communication_distances = LargestCommunicationDistances(client)
    """
    ENDPOINT = "/sc/largest-communication-distances"
    SINGLE_MODEL = LargestCommunicationDistances


class FastestIndividualCommunications(BaseAPICall):
    """
    A class for interacting with the fastest individual communications endpoint
    of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.sc import FastestIndividualCommunications
    >>> client = SeshatAPI()
    >>> fastest_individual_communications = FastestIndividualCommunications(client)
    """
    ENDPOINT = "/sc/fastest-individual-communications"
    SINGLE_MODEL = FastestIndividualCommunications
