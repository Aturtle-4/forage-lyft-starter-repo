from datetime import datetime

from engine.willoughby_engine import WilloughbyEngine

from engine.spindler_battery import Spindlerbattery
class Glissade(WilloughbyEngine):
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced() or Spindlerbattery.needs_service():
            return True
        else:
            return False
