import pytest
from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application("C:\\Program Files (x86)\\GAS Softwares\\Free Address Book\\AddressBook.exe")
    request.addfinalizer(fixture.destroy)
    return fixture

def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("xlsx_"):
            testdata = load_from_xlsx(fixture)