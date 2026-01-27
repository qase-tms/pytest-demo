import os

from qase.pytest import qase


def test_bytes_attachment():
    qase.attach(
        (str.encode("This is a simple string attachment"), "text/plain", "simple.txt")
    )
    assert True


def test_file_attachment():
    current_directory = os.getcwd()
    qase.attach(f"{current_directory}/tests/examples/attachments/test-file.txt")
    assert True


def test_file_attachment_with_mime_type():
    current_directory = os.getcwd()
    qase.attach(
        (f"{current_directory}/tests/examples/attachments/test-file.txt", "text/plain")
    )
    assert True


@qase.step("Step with bytes attachment")
def step_with_bytes_attachment():
    qase.attach(
        (str.encode("This is a simple string attachment"), "text/plain", "simple.txt")
    )
    pass


def test_step_attachment():
    step_with_bytes_attachment()
    assert True
