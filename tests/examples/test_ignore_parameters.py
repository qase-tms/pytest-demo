import pytest
from qase.pytest import qase


@pytest.mark.parametrize("browser", ["chrome", "firefox"])
@pytest.mark.parametrize("user", ["user1", "user2"])
@qase.ignore_parameters("user", "browser")
def test_ignore_multiple_parameters(browser, user):
    assert browser in ["chrome", "firefox"]
    assert user in ["user1", "user2"]


@pytest.mark.parametrize("browser", ["chrome", "firefox"])
@pytest.mark.parametrize("user", ["user1", "user2"])
@pytest.mark.parametrize("env", ["staging", "production"])
@qase.ignore_parameters("user")
def test_ignore_single_parameter(browser, user, env):
    assert browser in ["chrome", "firefox"]
    assert user in ["user1", "user2"]
    assert env in ["staging", "production"]


@qase.parametrize_ignore("test_data", ["data1", "data2"])
@pytest.mark.parametrize("browser", ["chrome", "firefox"])
@qase.ignore_parameters("browser")
def test_combined_ignore_decorators(browser, test_data):
    assert browser in ["chrome", "firefox"]
    assert test_data in ["data1", "data2"]
