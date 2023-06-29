from datetime import datetime

from engine.sternman_engine import SternmanEngine

from engine.spindler_battery import Spindlerbattery
class Palindrome(SternmanEngine):
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced() or Spindlerbattery.needs_service():
            return True
        else:
            return False
