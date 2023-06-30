from tires.tires import Tires
class Carigantire (Tires):
    def __init__ (self,sensor_val):
        self.current_sensor_val = sensor_val
    def needs_service(self):
        for i in self.current_sensor_val :
            if i >0.9:
                break
        else:
            return False
        return True