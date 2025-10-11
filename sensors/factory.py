from typing import Any, Dict, Type

from peripherals.factory_mapping import FactoryMapping
from peripherals.peripheral_factory import PeripheralFactory
from peripherals.peripheral_type import PeripheralType
from peripherals.sensors.digital_i2c_combo_sensor.config import DigitalComboConfig
from peripherals.sensors.digital_i2c_combo_sensor.digital_combo_drivers import DigitalComboDrivers
from peripherals.sensors.digital_i2c_combo_sensor.simulator import DigitalComboSimulator
from peripherals.sensors.digital_temp_sensors.config import DigitalTempConfig
from peripherals.sensors.digital_temp_sensors.digital_temp_drivers import DigitalTempDrivers
from peripherals.sensors.digital_temp_sensors.simulator import DigitalTempSimulator
from peripherals.sensors.tds_sensors.config import TDSConfig
from peripherals.sensors.tds_sensors.simulator import TDSSimulator
from peripherals.sensors.tds_sensors.tds_drivers import TDSDrivers
from peripherals.sensors.temperature_switch.config import TempSwitchConfig
from peripherals.sensors.temperature_switch.simulator import TempSwitchSimulator
from peripherals.sensors.temperature_switch.temp_switch_drivers import TempSwitchDrivers

class SensorFactory(PeripheralFactory):

    def __init__(self):
        super().__init__(folder_path='sensors', peripheral_type=PeripheralType.Sensor)

    _config_map: Dict[Type[Any], FactoryMapping] = {
        TDSConfig:              FactoryMapping.create(TDSSimulator,          'tds_sensors',              TDSDrivers),
        TempSwitchConfig:       FactoryMapping.create(TempSwitchSimulator,   'temperature_switch',       TempSwitchDrivers),
        DigitalTempConfig:      FactoryMapping.create(DigitalTempSimulator,  'digital_temp_sensors',     DigitalTempDrivers),
        DigitalComboConfig:     FactoryMapping.create(DigitalComboSimulator, 'digital_i2c_combo_sensor', DigitalComboDrivers),
    }

    def get_details(self, config:Any) -> 'FactoryMapping': 
        mapping = self._config_map.get(type(config))
        if not mapping:
            raise Exception(f"Unsupported sensor config type: {type(config)}")
        return mapping

