import pytest
from qase.pytest import qase

def test_qase_id():
    """This test will map dynamically to a single Qase ID"""
    assert True

def test_multiple_qase_id():
    """This test will map dynamically to multiple Qase IDs"""
    assert True

@pytest.mark.parametrize("role", ["admin", "user", "guest"])
def test_login_by_role(role):
    """Parameterized test, dynamic Qase ID mapping"""
    assert True
