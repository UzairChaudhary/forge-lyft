import unittest
from datetime import date

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class TestEngine(unittest.TestCase):
    def test_capulet_engine_needs_service(self):
        last_service_date = date.today()
        current_mileage = 50000
        last_service_mileage = 20000

        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_capulet_engine_does_not_need_service(self):
        last_service_date = date.today()
        current_mileage = 40000
        last_service_mileage = 20000

        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

    def test_sternman_engine_needs_service(self):
        last_service_date = date.today()
        warning_light_is_on = True

        engine = SternmanEngine(last_service_date, warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_sternman_engine_does_not_need_service(self):
        last_service_date = date.today()
        warning_light_is_on = False

        engine = SternmanEngine(last_service_date, warning_light_is_on)
        self.assertFalse(engine.needs_service())

    def test_willoughby_engine_needs_service(self):
        last_service_date = date.today()
        current_mileage = 70000
        last_service_mileage = 40000

        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_willoughby_engine_does_not_need_service(self):
        last_service_date = date.today()
        current_mileage = 50000
        last_service_mileage = 40000

        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())


if __name__ == '__main__':
    unittest.main()
