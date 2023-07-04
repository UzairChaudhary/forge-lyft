from tires.tires import Tires


class OctoprimeTires(Tires):
    def needs_service(self, tire_wear_array):
        return sum(tire_wear_array) >= 3