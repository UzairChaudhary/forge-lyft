import unittest
from datetime import date

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

class TestBattery(unittest.TestCase):
    def test_nubbin_battery_needs_service(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 4)
        current_date = today

        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_nubbin_battery_does_not_need_service(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 2)
        current_date = today

        battery = NubbinBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())

    def test_spindler_battery_needs_service(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 2)
        current_date = today

        battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_spindler_battery_does_not_need_service(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 1)
        current_date = today

        battery = SpindlerBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())


if __name__ == '__main__':
    unittest.main()
