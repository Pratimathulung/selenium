import pytest


@pytest.yield_fixture()
def setUp():
    print("Running confest demo2 method setUp")
    yield
    print("Running confest demo3 method tearDown")

@pytest.yield_fixture(scope='module')
def oneTimeSetUp():
    print("Running confest demo one time setUp")
    yield
    print("Running confest demo one time tearDown")
