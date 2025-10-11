from threading import RLock
from typing import Any, List, Optional

from peripherals.actuators.actuator import Actuator
from peripherals.actuators.factory import ActuatorFactory
from peripherals.communication.analog_digital_converter.adc_driver import ADCDriver
from peripherals.communication.communication import Communication
from peripherals.communication.factory import CommunicationFactory
from peripherals.catalog.catalog_category import CatalogCategory
from peripherals.communication.i2c_multiplexer.connection import MultiplexerConnection
from peripherals.communication.i2c_multiplexer.i2c_multiplexer_driver import I2CMultiplexerDriver
from peripherals.peripheral_type import PeripheralType
from peripherals.sensors.sensor import Sensor
from peripherals.sensors.factory import SensorFactory
from peripherals.utilities.object_scanner import ObjectScanner
from src.contracts.modules.analog_base import AnalogBase
from src.contracts.modules.i2c_base import I2CBase

class DeviceCatalog:

    _lock:RLock = None

    sensors:CatalogCategory[Sensor] = None
    actuators:CatalogCategory[Actuator] = None
    communication_modules:CatalogCategory[Communication] = None

    @property
    def peripherals(self) -> List[Any]:
        with self._lock:
            return self.sensors.all + self.actuators.all + self.communication_modules.all
        
    def register_i2c_configuration(self, device_name:str, i2c_configuration:I2CBase):
        if i2c_configuration.multiplexer_details is None:
            return None        
    
        mux:I2CMultiplexerDriver = self.communication_modules.get_by_name(i2c_configuration.multiplexer_details.name, I2CMultiplexerDriver)
        if mux is None:
            raise Exception(f"I2C Multiplexer '{i2c_configuration.multiplexer_details.name}' not found in catalog.")
        i2c_configuration.multiplexer_details.set_multiplexer(mux)

        connection = MultiplexerConnection.create(device_name, i2c_configuration.i2c_address, i2c_configuration.multiplexer_details.channel)
        mux.add_connection(connection)

    def register_adc_configuration(self, adc_configuration:AnalogBase) -> None:
        if adc_configuration.adc_details is not None:
            adc = self.communication_modules.get_by_name(adc_configuration.adc_details.name, ADCDriver)
            if adc is None:
                raise Exception(f"ADC Module '{adc_configuration.adc_details.name}' not found in catalog.")
            adc_configuration.adc_details.set_adc_module(adc)

    def _register(self, peripheral_type:PeripheralType, configurations:List[Any], factory_type:Any, is_simulated:bool, scan_for_i2c:bool, scan_for_adc:bool) -> None:
        factory = factory_type()

        for config in configurations:            
            peripheral = factory.create(config, simulate=is_simulated)

            if scan_for_i2c:
                i2c_configuration = ObjectScanner.find_single_or_default(config, I2CBase)
                if i2c_configuration is not None:
                    self.register_i2c_configuration(peripheral.key, i2c_configuration)

            if scan_for_adc:
                adc_configuration = ObjectScanner.find_single_or_default(config, AnalogBase)
                if adc_configuration is not None:
                    self.register_adc_configuration(peripheral.key, adc_configuration)

            if peripheral_type == PeripheralType.Sensor:
                self.sensors.register(peripheral)
            elif peripheral_type == PeripheralType.Actuator:
                self.actuators.register(peripheral)
            elif peripheral_type == PeripheralType.Communication:
                self.communication_modules.register(peripheral) 
            else:
                raise Exception(f'Unsupported peripheral type: {peripheral_type}')


    def __init__(self,
            is_simulated:bool = False,           
            sensors_config:Optional[List[Any]] = None,
            actuators_config:Optional[List[Any]] = None,                 
            communications_config:Optional[List[Any]] = None   
        ):
    
        self._lock = RLock()
        self.sensors = CatalogCategory[Sensor]()
        self.actuators = CatalogCategory[Actuator]()
        self.communication_modules = CatalogCategory[Communication]()

        if communications_config is not None:
            self._register(
                peripheral_type=PeripheralType.Communication,                 
                configurations=communications_config, 
                factory_type=CommunicationFactory, 
                is_simulated=is_simulated, 
                scan_for_i2c=False, 
                scan_for_adc=False)
        
        if sensors_config is not None:
            self._register(
                peripheral_type=PeripheralType.Sensor,                 
                configurations=sensors_config, 
                factory_type=SensorFactory, 
                is_simulated=is_simulated, 
                scan_for_i2c=True, 
                scan_for_adc=False)

        if actuators_config is not None:
            self._register(
                peripheral_type=PeripheralType.Actuator,                 
                configurations=actuators_config, 
                factory_type=ActuatorFactory, 
                is_simulated=is_simulated, 
                scan_for_i2c=True, 
                scan_for_adc=False)

        
