from datetime import datetime
from typing import Any, TypeVar, Generic
from dataclasses import dataclass

from peripherals.sensors.sensor_type import SensorType
from peripherals.sensors.unit_type import UnitType

T = TypeVar('T')


@dataclass
class SensorReading(Generic[T]):
    value: T
    device_name:str = None
    sensor_type: SensorType = None
    driver_name: str = None
    read_time: datetime = None
    unit_type: UnitType = None

    @property
    def description(self) -> str:
        return self.__str__()

    def __str__(self):
        unit_measure = ''
        if (self.unit_type != None and self.unit_type != UnitType.Unkown):
            unit_measure = f' {self.unit_type.value}'

        reading = f'{self.device_name}: >>> {self.value}{unit_measure} <<< '
        details = f'(Sensor: {self.sensor_type.name}, Driver: {self.driver_name}) read @{self.read_time}'         

        return f'{reading}{details}'
    
    @staticmethod
    def create(value: T, sensor: Any, date_time:datetime = datetime.utcnow()) -> 'SensorReading[T]':
        return SensorReading(value=value, sensor_type=sensor.sensor_type, driver_name=sensor.driver_name, device_name= sensor.name, unit_type=sensor.unit_type, read_time=date_time)
