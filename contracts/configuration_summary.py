
from typing import List
from pydantic import BaseModel

from peripherals.actuators.actuator import Actuator
from peripherals.communication.analog_digital_converter.adc_module import ADCModule
from peripherals.communication.i2c_multiplexer.i2c_multiplexer import I2CMultiplexer
from peripherals.contracts.device_type import DeviceType
from peripherals.contracts.pin_config import PinConfig
from peripherals.sensors.sensor import Sensor

class ConfigurationSummary(BaseModel):
    device_type:DeviceType = None
    pin_configurations: List[PinConfig] = None
    sensors: List[Sensor] = None
    actuators: List[Actuator] = None
    i2c_multiplexers: List[I2CMultiplexer] = None
    adc_modules: List[ADCModule] = None
    warnings: List[str] = None

    class Config:
        arbitrary_types_allowed = True

    @staticmethod
    def create(
        device_type:DeviceType,
        pin_configurations: List[PinConfig] = None,
        sensors: List[Sensor] = None,
        actuators: List[Actuator] = None,
        i2c_multiplexers: List[I2CMultiplexer] = None,
        adc_modules: List[ADCModule] = None,
        warnings: List[str] = None
    ) -> 'ConfigurationSummary':

        return ConfigurationSummary(
            device_type=device_type,
            pin_configurations=pin_configurations if pin_configurations is not None else [],
            sensors=sensors if sensors is not None else [],
            actuators=actuators if actuators is not None else [],
            i2c_multiplexers=i2c_multiplexers if i2c_multiplexers is not None else [],
            adc_modules=adc_modules if adc_modules is not None else [],
            warnings=warnings if warnings is not None else []
        )