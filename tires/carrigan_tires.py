from tires.tires import Tires
class CarriganTires(Tires):
    def needs_service(self, tire_wear_array):
        return any(wear >= 0.9 for wear in tire_wear_array)
