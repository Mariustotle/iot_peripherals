
from abc import abstractmethod
from peripherals.peripheral import Peripheral
from peripherals.peripheral_type import PeripheralType
from peripherals.sensors.sensor_reading import SensorReading
from peripherals.sensors.sensor_type import SensorType
from typing import TypeVar

from peripherals.sensors.unit_type import UnitType

T = TypeVar('T')

class Sensor(Peripheral):
    sensor_type: SensorType = None
    unit_type: UnitType = None
    driver_name:str = None
    
    def __init__(self, sensor_type:SensorType, name:str, driver_name:str, unit_type:UnitType = UnitType.Unkown):        
        super().__init__(PeripheralType.Sensor, name)

        self.sensor_type = sensor_type
        self.driver_name = driver_name
        self.unit_type = unit_type

    @abstractmethod
    async def read(self) -> SensorReading[T]: pass