from abc import abstractmethod
import asyncio
from datetime import datetime
from peripherals.sensors.sensor import Sensor
from peripherals.sensors.sensor_types import SensorType
from peripherals.sensors.tds_sensors.tds_config import TDSConfig
from peripherals.sensors.tds_sensors.tds_drivers import TDSDrivers


class TDSDriverBase(Sensor):
    config:TDSConfig = None
    simulated:bool = None
    
    def __init__(self, config:TDSConfig, simulated:bool = False):
        driver = config.driver if config.driver is not None else TDSDrivers.Default
        driver_name = driver.value if not simulated else 'N/A - Simulated'

        super().__init__(SensorType.TDS, config.name, driver_name)
        
        self.config = config
        self.simulated = simulated 

        if (not self.validate(config)):
            raise Exception(f'Unable to instanciate communication driver [{self.driver_name}] as the config validation failed.')        

    # Can be overrided in driver specific implimentation for special rules
    def validate(self, config:TDSConfig) -> bool:  return True

    @abstractmethod
    async def read_once(self) -> float: pass

    async def read(self) -> float:
        total = 0.0

        for take in range (0, self.config.number_of_readings):
            total += await self.read_once()

            if (take < self.config.number_of_readings and self.config.delay_between_readings > 0):
                import time
                asyncio.wait_for(self.config.delay_between_readings)

        average = total / self.config.number_of_readings
        self.latest_reading = average
        self.last_updated = datetime.utcnow()
        return average


    def get_description(self) -> str: 
        return f"Peripheral: [{self.peripheral_type.name}], Communication: [{self.sensor_type.name}], Driver: [{self.driver_name}] with configuration of XXXXXXXX."




