from qase.pytest import qase


@qase.id(1)
def test_qase_id():
    assert True


@qase.id([2, 3])
def test_multiple_qase_id():
    assert True


@qase.id(31)
@qase.title("QA-3938 | TC1 -> SuperUser can add new Note | SuperUser")
def test_superuser_can_add_new_note():
    assert True
