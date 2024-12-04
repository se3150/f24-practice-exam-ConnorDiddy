import pytest
from battery import Battery
from unittest.mock import Mock

todo = pytest.mark.skip(reason='todo: pending spec')

@pytest.fixture
def charged_battery():
    return Battery(100)

@pytest.fixture
def partially_charged_battery():
    b = Battery(100)
    b.mCharge = 70
    return b

@pytest.fixture
def battery_with_monitor():
    monitor = Mock()
    battery = Battery(100, external_monitor=monitor)
    return battery, monitor

def describe_Battery():

    def describe_recharge():
        def test_recharge_increases_charge(partially_charged_battery):
            partially_charged_battery.recharge(20)
            assert partially_charged_battery.getCharge() == 90

        def test_recharge_does_not_exceed_capacity(partially_charged_battery):
            partially_charged_battery.recharge(50)
            assert partially_charged_battery.getCharge() == 100

        def test_recharge_with_invalid_amount(partially_charged_battery):
            assert not partially_charged_battery.recharge(-10)
            assert partially_charged_battery.getCharge() == 70

        def test_recharge_notifies_monitor(battery_with_monitor):
            battery, monitor = battery_with_monitor
            battery.mCharge = 50
            battery.recharge(30)
            monitor.notify_recharge.assert_called_once_with(80)

    def describe_drain():
        def test_drain_decreases_charge(partially_charged_battery):
            partially_charged_battery.drain(20)
            assert partially_charged_battery.getCharge() == 50

        def test_drain_does_not_go_below_zero(partially_charged_battery):
            partially_charged_battery.drain(80)
            assert partially_charged_battery.getCharge() == 0

        def test_drain_with_invalid_amount(partially_charged_battery):
            assert not partially_charged_battery.drain(-10)
            assert partially_charged_battery.getCharge() == 70

        def test_drain_notifies_monitor(battery_with_monitor):
            battery, monitor = battery_with_monitor
            battery.mCharge = 50
            battery.drain(30)
            monitor.notify_drain.assert_called_once_with(20)

    def describe_getCapacity():
        def test_getCapacity(charged_battery):
            assert charged_battery.getCapacity() == 100
            
    def describe_getCharge():
        def test_getCharge(charged_battery):
            assert charged_battery.getCharge() == 100