from qase.pytest import qase


@qase.suite("First suite")
def test_suite():
    assert True


@qase.suite("First suite", "This is a suite description")
def test_suite_with_description():
    assert True


@qase.suite("First suite\tSecond Suite")
def test_suite_nesting_1():
    assert True


@qase.suite("First suite.Second Suite.Third Suite")
def test_suite_nesting_2():
    assert True
