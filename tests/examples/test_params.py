import pytest
from qase.pytest import qase


# -----------------------------
# Basic test with single params
# -----------------------------

@pytest.mark.parametrize("Parameter", ["Value 1", "Value 2"])
def test_with_parameter(Parameter: str):
    """
    Runs the same test with two different string values.
    Logs nothing explicitly to Qase (Qase will capture the parameter implicitly).
    """
    assert Parameter in ["Value 1", "Value 2"]
    print(f"Test executed with parameter: {Parameter}")


# ----------------------------------------
# Test with Multiple group parameters 
# ----------------------------------------

@pytest.mark.parametrize(
    "username, password",
    [
        pytest.param("@alice", "pass123", id="Alice B"),
        pytest.param("@bob", "pass456", id="Bob C"),
    ],
)
def test_group_parameters(username: str, password: str):
    """
    Simulates login attempts with different user credentials.
    IDs improve readability in test reports.
    """
    assert isinstance(username, str)
    assert isinstance(password, str)

    if username == "@alice":
        assert password == "pass123"
    elif username == "@bob":
        assert password == "pass456"

    print(f"Test executed for user: {username} with password: {password}")


# -------------------------------------------
# Manually adding params with qase.params() 
# -------------------------------------------

def test_manual_qase_params():
    """
    Logs fixed parameters manually using qase.param.
    Useful when values are internal or not passed to the function.
    """
    qase.param("env", "staging")
    qase.param("feature", "login")

    assert True
    print("Test executed with manually logged Qase parameters")


# ---------------------------------------------------------
# Dynamic parameter logging using test input (parametrize)
# ---------------------------------------------------------

@pytest.mark.parametrize("env", ["dev", "qa", "prod"])
def test_dynamic_qase_param(env: str):
    """
    Captures and logs runtime parameter passed via pytest.
    """
    qase.param("env", env)

    assert env in ["dev", "qa", "prod"]
    print(f"Test executed in environment: {env}")


# ---------------------------------------------------------------------------------------
# A test where one parameter is IGNORED and doesn't show up in the Qase test run
# ---------------------------------------------------------------------------------------

@pytest.mark.parametrize("email", ["@abc", "@xyz", "@asdf"])
@pytest.mark.parametrize("role", ["admin", "user"])

@qase.parametrize_ignore("role", ["admin", "user"])
def test_with_ignored_param(browser, role):
    """
    'email' will appear in Qase reports.
    'role' is used in the test but not reported to Qase.
    """
    assert browser in ["@abc", "@xyz", "@asdf"]
    assert role in ["admin", "user"]


# ---------------------------------------------------------------------------------------
# A test where one indirect parameter is IGNORED and doesn't show up in the Qase test run
# ---------------------------------------------------------------------------------------

@pytest.fixture
def test_data(request):
    return ["data1", "data2"]

# Parametrize emails
@pytest.mark.parametrize("email", ["@abc", "@xyz", "@asdf"])

@qase.parametrize_ignore("test_data", ["data1", "data2"], indirect=True)

def test_with_ignored_param(email, test_data):
    """
    'email' will appear in Qase reports.
    'test_data' is used in the test but ignored in Qase.
    """
    assert email in ["@abc", "@xyz", "@asdf"]
    assert test_data == ["data1", "data2"]  # compare directly to the fixture output

    print(f"Test executed on email: {email} with test data: {test_data}")