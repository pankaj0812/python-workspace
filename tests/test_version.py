# test_version.py

from src import __version__


def test_version():
    assert __version__ == "1.0"
