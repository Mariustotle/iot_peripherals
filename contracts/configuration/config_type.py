from enum import Enum

from peripherals.actuators.relay_switches.config import RelayConfig
from peripherals.contracts.configuration.class_mapping import ClassMapping
from peripherals.peripheral_type import PeripheralType
from peripherals.sensors.tds_sensors.config import TDSConfig
from peripherals.sensors.temperature_sensors.config.analog_config import AnalogTemperatureConfig
from peripherals.sensors.temperature_sensors.config.digital_config import DigitalTemperatureConfig
from peripherals.sensors.temperature_sensors.config.digital_i2c_config import DigitalI2CTemperatureConfig
from peripherals.sensors.temperature_switch.config import TempSwitchConfig

class ConfigType(ClassMapping, Enum):

    # ACTUATORS
    # --------------------------------------------------------------------------------------------------

    RelaySwitch                     = ("RelaySwitch",                       PeripheralType.Actuator,    RelayConfig)     

    # SENSORS
    # --------------------------------------------------------------------------------------------------

    ## TDS Sensors
    TDSSensor                       = ("TDSSensor",                         PeripheralType.Sensor,      TDSConfig)

    ## Temperature Sensors
    AnalogTemperatureSensor         = ("AnalogTemperatureSensor",           PeripheralType.Sensor,      AnalogTemperatureConfig)
    DigitalTemperatureSensor        = ("DigitalTemperatureSensor",          PeripheralType.Sensor,      DigitalTemperatureConfig)
    DigitalI2CTemperatureSensor     = ("DigitalI2CTemperatureSensor",       PeripheralType.Sensor,      DigitalI2CTemperatureConfig)

    ## Temperature Switches
    TemperatureSwitch               = ("TemperatureSwitch",                 PeripheralType.Sensor,      TempSwitchConfig)