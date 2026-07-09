from tracking_status_normalizer.governance.coverage.capability import (
    Capability,
)


def test_capabilities_exist():
    assert Capability.DIRECT_DELIVERY.value == "DIRECT_DELIVERY"

    assert Capability.PUDO.value == "PUDO"

    assert Capability.LOCKER.value == "LOCKER"

    assert (
        Capability.OUT_OF_HOME_DELIVERY.value
        == "OUT_OF_HOME_DELIVERY"
    )

    assert Capability.RETURNS.value == "RETURNS"

    assert Capability.CUSTOMS.value == "CUSTOMS"

    assert (
        Capability.EXCEPTION_MANAGEMENT.value
        == "EXCEPTION_MANAGEMENT"
    )