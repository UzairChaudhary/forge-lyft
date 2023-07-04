import unittest
from datetime import date

from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires

class TestTires(unittest.TestCase):
    def setUp(self):
        self.carrigan_tires = CarriganTires()
        self.octoprime_tires = OctoprimeTires()

    def test_carrigan_tires_needs_service(self):
        tire_wear_array = [0.8, 0.9, 0.7, 0.95]
        self.assertTrue(self.carrigan_tires.needs_service(tire_wear_array))

    def test_carrigan_tires_no_service_required(self):
        tire_wear_array = [0.8, 0.6, 0.7, 0.85]
        self.assertFalse(self.carrigan_tires.needs_service(tire_wear_array))

    def test_octoprime_tires_needs_service(self):
        tire_wear_array = [0.5, 1.2, 0.8, 0.5]
        self.assertTrue(self.octoprime_tires.needs_service(tire_wear_array))

    def test_octoprime_tires_no_service_required(self):
        tire_wear_array = [0.5, 0.5, 0.5, 0.5]
        self.assertFalse(self.octoprime_tires.needs_service(tire_wear_array))


if __name__ == '__main__':
    unittest.main()