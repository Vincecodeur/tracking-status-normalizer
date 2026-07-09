from tracking_status_normalizer.governance.maturity.maturity_level import (
    MaturityLevel,
)


def test_maturity_levels():
    assert MaturityLevel.BASIC.value == "BASIC"
    assert MaturityLevel.DEVELOPING.value == "DEVELOPING"
    assert MaturityLevel.MATURE.value == "MATURE"
    assert MaturityLevel.ADVANCED.value == "ADVANCED"