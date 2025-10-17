import pytest
from qase.pytest import qase

@qase.tags("tag1", "tag2")
def test_qase_tags():
    assert True