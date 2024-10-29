from pytest import raises
from seshat_api import SeshatAPI, get_variable_classes, get_variable_name, seshat_class_instance, get_frequencies


def test_get_variable_name():
    assert get_variable_name("Camels") == "camel"
    assert get_variable_name("ExampleClasses") == "example_class"
    assert get_variable_name("BigPonies") == "big_pony"
    assert get_variable_name("AlreadySingular") == "already_singular"
    assert get_variable_name("Judges") == "judge"


def test_seshat_class_instance():
    # Assert this does not raise an error
    seshat_class_instance("ProfessionalSoldiers", "professional_soldier")
    
    # Assert this raises an ImportError
    with raises(ImportError):
        seshat_class_instance("FakeClasses", "fake_class")


def test_get_variable_classes():
    vc = get_variable_classes()
    assert "ProfessionalSoldiers" in vc
    assert "Judges" in vc
    assert "BigPonies" not in vc


def test_get_frequencies():
    client = SeshatAPI(base_url="https://seshatdata.com/api")
    class_names = ['Roads', 'ProfessionalSoldiers']
    years = range(0, 10)
    value = 'absent'
    df = get_frequencies(client, class_names, years, value)
    # Assert the df has 10 rows and 2 columns
    assert df.shape == (10, 2)
