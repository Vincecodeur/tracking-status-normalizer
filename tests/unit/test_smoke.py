"""Smoke tests to ensure the package is importable and healthy."""

from tracking_status_normalizer import __version__


def test_package_has_version() -> None:
    assert isinstance(__version__, str)
    assert __version__ != ""