
from datetime import date

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from car import Car

class CarFactory:
    def create_calliope(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        return Car(CapuletEngine(last_service_date, current_mileage, last_service_mileage),
                   SpindlerBattery(last_service_date, current_date))

    def create_glissade(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        return Car(WilloughbyEngine(last_service_date, current_mileage, last_service_mileage),
                   SpindlerBattery(last_service_date, current_date))

    def create_palindrome(self, current_date: date, last_service_date: date, warning_light_on: bool):
        return Car(SternmanEngine(last_service_date, warning_light_on),
                   SpindlerBattery(last_service_date, current_date))

    def create_rorschach(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        return Car(WilloughbyEngine(last_service_date, current_mileage, last_service_mileage),
                   NubbinBattery(last_service_date, current_date))

    def create_thovex(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        return Car(CapuletEngine(last_service_date, current_mileage, last_service_mileage),
                   NubbinBattery(last_service_date, current_date))