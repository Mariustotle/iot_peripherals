
from abc import abstractmethod
from datetime import datetime
from typing import Any, Optional
from peripherals.peripheral import Peripheral
from peripherals.peripheral_type import PeripheralType
from peripherals.sensors.sensor_types import SensorType

class Sensor(Peripheral):
    sensor_type: SensorType = None
    driver_name:str = None
    latest_reading: Optional[Any] = None
    last_updated: Optional[datetime] = None
    
    def __init__(self, sensor_type:SensorType, name:str, driver_name:str):        
        super().__init__(PeripheralType.Sensor, name)

        self.sensor_type = sensor_type
        self.driver_name = driver_name

    @abstractmethod
    def read_once(self): pass