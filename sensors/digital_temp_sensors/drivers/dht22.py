


import random
from peripherals.contracts.temperature_measurement import TemperatureMeasurement
from peripherals.sensors.digital_temp_sensors.driver_base import DigitalTempDriverBase

class LM3DHT2293(DigitalTempDriverBase):

    def _default_reading(self) -> float:

        # Assume typical room temperature range
        if self.config.measurement == TemperatureMeasurement.Celcious:
            # Room temperature between 18°C and 26°C
            return round(random.uniform(18.0, 26.0), 2)
        
        elif self.unit == "Fahrenheit":
            # Equivalent in Fahrenheit (65°F to 79°F)
            return round(random.uniform(65.0, 79.0), 2)

