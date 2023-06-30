from tires.tires import Tires
class Octoprimetire (Tires):
    def __init__ (self,sensor_val):
        self.current_sensor_val = sensor_val
    def needs_service(self):
        sum =0
        for i in self.current_sensor_val :
            sum+=i
        if sum >= 3:
            return True
        else:
            return False