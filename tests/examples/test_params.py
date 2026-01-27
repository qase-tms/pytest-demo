import pytest
from qase.pytest import qase


@pytest.mark.parametrize("Parameter", ["Value 1", "Value 2"])
def test_with_parameter(Parameter: str):
    assert Parameter in ["Value 1", "Value 2"]


@pytest.mark.parametrize(
    "username, password",
    [
        pytest.param("@alice", "pass123", id="Alice B"),
        pytest.param("@bob", "pass456", id="Bob C"),
    ],
)
def test_group_parameters(username: str, password: str):
    assert isinstance(username, str)
    assert isinstance(password, str)

    if username == "@alice":
        assert password == "pass123"
    elif username == "@bob":
        assert password == "pass456"


def test_manual_qase_params():
    qase.param("env", "staging")
    qase.param("feature", "login")
    assert True


@pytest.mark.parametrize("env", ["dev", "qa", "prod"])
def test_dynamic_qase_param(env: str):
    qase.param("env", env)
    assert env in ["dev", "qa", "prod"]


@pytest.mark.parametrize("email", ["@abc", "@xyz", "@asdf"])
@qase.parametrize_ignore("test_data", ["data1", "data2"])
def test_with_ignored_param(email, test_data):
    assert email in ["@abc", "@xyz", "@asdf"]
    assert test_data in ["data1", "data2"]
