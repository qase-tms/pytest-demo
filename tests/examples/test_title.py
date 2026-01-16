from qase.pytest import qase

@qase.id(1276)
@qase.title("This shall be the title of the test case")
def test_qase_title():
    assert True



@qase.id(6000)
@qase.title("This shall be the title of the test case")
def test_qase_title():
    assert True