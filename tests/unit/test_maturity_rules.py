from tracking_status_normalizer.governance.maturity.maturity_level import (
    MaturityLevel,
)
from tracking_status_normalizer.governance.maturity.maturity_rules import (
    determine_maturity_level,
)


def test_advanced():
    assert determine_maturity_level(95) == MaturityLevel.ADVANCED


def test_mature():
    assert determine_maturity_level(80) == MaturityLevel.MATURE


def test_developing():
    assert determine_maturity_level(60) == MaturityLevel.DEVELOPING


def test_basic():
    assert determine_maturity_level(40) == MaturityLevel.BASIC