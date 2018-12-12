import pytest


@pytest.mark.run(order=2)
def test_run_methodA(oneTimeSetUp, setUp):
    print("Running method A")


@pytest.mark.run(order=1)
def test_run_methodB(oneTimeSetUp, setUp):
    print("Running method B")


@pytest.mark.run(order=5)
def test_run_methodC(oneTimeSetUp, setUp):
    print("Running method C")


@pytest.mark.run(order=4)
def test_run_methodD(oneTimeSetUp, setUp):
    print("Running method D")


@pytest.mark.run(order=3)
def test_run_methodE(oneTimeSetUp, setUp):
    print("Running method E")


def test_run_methodF(oneTimeSetUp, setUp):
    print("Running method F")
