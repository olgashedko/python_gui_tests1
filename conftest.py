import os

import pytest
from comtypes.client import CreateObject

from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application("C:\\Users\\Olechka\\FreeAddressBookPortable\\AddressBook.exe")
    request.addfinalizer(fixture.destroy)
    return fixture


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("xlsx_"):
            testdata = load_from_xlsx(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_xlsx(file):
    f = os.path.join(os.path.dirname(os.path.abspath(__file__)), "%s.xlsx" % file)
    x1 = CreateObject("Excel.Application", dynamic=True)
    x1.Visible = True
    wb = x1.Workbooks.Open(f)
    testdata = x1.Range["A%s:A%s" % (1, 10)].Value()
    x1.Quit()
    return testdata
