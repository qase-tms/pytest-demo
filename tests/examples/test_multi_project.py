import pytest
from qase.pytest import qase


@qase.project_id("PROJ1", 1)
def test_single_project_single_id():
    assert True


@qase.project_id("PROJ1", [2, 3])
def test_single_project_multiple_ids():
    assert True


@qase.project_id("PROJ1", 4)
@qase.project_id("PROJ2", 10)
def test_multiple_projects_single_id():
    assert True


@qase.project_id("PROJ1", [5, 6])
@qase.project_id("PROJ2", [11, 12])
def test_multiple_projects_multiple_ids():
    assert True


@qase.project_id("PROJ2", 13)
def test_multiple_projects():
    assert True


@qase.project_id("PROJ1", 9)
@qase.title("User Login Test")
@qase.fields(
    ("severity", "critical"),
    ("priority", "high")
)
def test_with_other_decorators():
    assert True


def test_without_id():
    assert True
