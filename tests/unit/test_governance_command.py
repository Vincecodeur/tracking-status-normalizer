"""
Tests for governance CLI command.
"""

from tracking_status_normalizer.cli.commands import (
    governance_command,
)


def test_governance_command_markdown():
    result = governance_command(
        "markdown"
    )

    assert result == 0


def test_governance_command_json():
    result = governance_command(
        "json"
    )

    assert result == 0


def test_governance_command_csv():
    result = governance_command(
        "csv"
    )

    assert result == 0


def test_governance_command_html():
    result = governance_command(
        "html"
    )

    assert result == 0


def test_governance_command_invalid_format():
    result = governance_command(
        "invalid"
    )

    assert result == 1