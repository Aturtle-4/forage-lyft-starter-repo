from abc import ABC
from datetime import datetime
from car import Car
class Spindlerbattery(Car, ABC):
    def __init__(self, last_service_date, warning_light_is_on):
        super().__init__(last_service_date)
        self.currentdate = datetime.today().date()
    def needs_service(self):
        if self.currentdate - self.last_service_date >=2:
            return True
        else:
            return False