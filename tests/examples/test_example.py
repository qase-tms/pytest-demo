from qase.pytest import qase
import pytest
def test_example():
    qase.param("foo", "bar")
    qase.param("baz", "qux")
    pass

def test_example(param1: str):
    qase.param("param1", param1)
    pass    