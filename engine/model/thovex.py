from datetime import datetime

from engine.capulet_engine import CapuletEngine

from engine.nubblin_battery import Nubblinbattery
class Thovex(CapuletEngine):
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced() or Nubblinbattery.needs_service():
            return True
        else:
            return False
