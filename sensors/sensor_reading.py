from datetime import datetime
from typing import Any, Optional, TypeVar, Generic
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

    def __str__(self) -> str:
       
        unit_measure = ''
        if (self.unit_type != None and self.unit_type != UnitType.Unkown):
            unit_measure = f' {self.unit_type.value}'

        converted_value = str(self.value)

        return f'>>> {converted_value} <<< @ {self.read_time}'        

    
    @staticmethod
    def create(value: T, sensor: Any, read_time:Optional[datetime] = None) -> 'SensorReading[T]':

        if (read_time is None):
            read_time = datetime.utcnow()

        sensor.last_read_time = read_time

        return SensorReading(value=value, sensor_type=sensor.sensor_type, driver_name=sensor.driver_name, device_name= sensor.name, unit_type=sensor.unit_type, read_time=read_time)
