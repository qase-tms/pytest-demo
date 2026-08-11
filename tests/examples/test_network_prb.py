import time
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


# --- Load generator ---------------------------------------------------------
# ~300 results, each with a small artificial delay, so the whole run takes
# roughly 30-60 seconds with -n 4. That gives you a window to flip your VPN
# off and back on partway through, while results are actively being sent
# to Qase in the background.
@pytest.mark.parametrize("case_id", range(1, 301))
def test_bulk_case(case_id):
    """Slow-ish trivial test used to stretch run time and inflate result count."""
    time.sleep(0.4)  # tune this up/down to make the run longer/shorter
    assert case_id > 0