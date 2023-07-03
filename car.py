from abc import ABC, abstractmethod

class Car:
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery
    @abstractmethod
    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
