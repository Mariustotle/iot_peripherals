from threading import RLock
from typing import Any, List, Optional

from peripherals.actuators.actuator import Actuator
from peripherals.actuators.factory import ActuatorFactory
from peripherals.communication.analog_digital_converter.adc_module import ADCModule
from peripherals.communication.communication import Communication
from peripherals.communication.factory import CommunicationFactory
from peripherals.catalog.catalog_category import CatalogCategory
from peripherals.communication.i2c_multiplexer.connection import MultiplexerConnection
from peripherals.communication.i2c_multiplexer.i2c_multiplexer import I2CMultiplexer
from peripherals.contracts.adapter_type import AdapterType
from peripherals.contracts.configuration.config_base import ConfigBase
from peripherals.contracts.configuration.configuration_summary import ConfigurationSummary
from peripherals.contracts.device_type import DeviceType
from peripherals.contracts.pins.pin_config import PinConfig
from peripherals.devices.device_base import DeviceBase
from peripherals.peripheral_type import PeripheralType
from peripherals.sensors.sensor import Sensor
from peripherals.sensors.factory import SensorFactory
from peripherals.utilities.object_scanner import ObjectScanner
from src.contracts.modules.analog_base import AnalogBase
from src.contracts.modules.i2c_base import I2CBase

class DeviceCatalog:

    _lock:RLock = None
    
    device:Optional[DeviceBase] = None
    simulated:bool = None
    device_type:DeviceType = None
    adapter_type:AdapterType = None
    pin_configurations:List[PinConfig] = None
    sensors:CatalogCategory[Sensor] = None
    actuators:CatalogCategory[Actuator] = None
    communication_modules:CatalogCategory[Communication] = None

    warnings:List[str] = None

    @property
    def peripherals(self) -> List[Any]:
        with self._lock:
            return self.sensors.all + self.actuators.all + self.communication_modules.all
        
    def validate(self):

        if self.communication_modules is not None or len(self.communication_modules.all) > 0:
            for comm in self.communication_modules.all:
                if isinstance(comm, I2CMultiplexer) and len(comm.connections) == 0:
                    self.warnings.append(f'I2C Multiplexer [{comm.key}] has no connected devices.')

                if isinstance(comm, ADCModule) and len(comm.connections) == 0:
                    self.warnings.append(f'ADC Module [{comm.key}] has no connected devices.')


    def get_device_configuration_summary(self) -> 'ConfigurationSummary':

        summary = ConfigurationSummary.create(
            device_type=self.device_type,            
            pin_configurations=self.pin_configurations,
            sensors=self.sensors.all,
            actuators=self.actuators.all,
            i2c_multiplexers=[comm for comm in self.communication_modules.all if isinstance(comm, I2CMultiplexer)],
            adc_modules=[comm for comm in self.communication_modules.all if isinstance(comm, ADCModule)],
            warnings=self.warnings
        )

        return summary
        
    def register_i2c_configuration(self, device_name:str, i2c_configuration:I2CBase):
        if i2c_configuration.multiplexer_details is None:
            return None        
    
        mux:I2CMultiplexer = self.communication_modules.get_by_name(i2c_configuration.multiplexer_details.name, I2CMultiplexer)
        if mux is None:
            raise Exception(f"I2C Multiplexer '{i2c_configuration.multiplexer_details.name}' not found in catalog.")
        i2c_configuration.multiplexer_details.set_multiplexer(mux)

        connection = MultiplexerConnection.create(device_name, i2c_configuration.i2c_address, i2c_configuration.multiplexer_details.channel)
        mux.add_connection(connection)

    def register_adc_configuration(self, adc_configuration:AnalogBase) -> None:
        if adc_configuration.adc_details is not None:
            adc = self.communication_modules.get_by_name(adc_configuration.adc_details.name, ADCModule)
            if adc is None:
                raise Exception(f"ADC Module '{adc_configuration.adc_details.name}' not found in catalog.")
            adc_configuration.adc_details.set_adc_module(adc)

    def _register_pin(self, source:str, counter:int, pin_config:PinConfig) -> None:
        if pin_config is None:
            return

        if pin_config.name is None or pin_config.name == '':
            pin_config.name = f'{source} (pin-{counter})'

        existing = next((p for p in self.pin_configurations if p.pin == pin_config.pin and p.scheme == pin_config.scheme), None)
        if existing:
            raise Exception(f"Pin conflict detected for [{pin_config.name}]: Pin [{pin_config.pin}] with scheme [{pin_config.scheme.name}] is already registered as [{existing.name}].")
        
        (position, pin_details) = self.device.get_gpio_pin(pin_config.pin, pin_config.scheme)

        if (pin_details is None):
            raise Exception(f"Pin [{pin_config.pin}] with scheme [{pin_config.scheme.name}] for [{pin_config.name}] is not available on the device.")
        
        if pin_details.in_use:
            raise Exception(f"Pin [{pin_config.pin}] with scheme [{pin_config.scheme.name}] for [{pin_config.name}] is already in use.")
        
        #TODO: Move this to device pin configuration - The type must be set by the driver pin registration not the config
        self.device.associate_pin(position, None)

        self.pin_configurations.append(pin_config)

    def _register_peripheral(self, peripheral_type:PeripheralType, config:ConfigBase, factory_type:Any, is_simulated:bool) -> None:
        factory = factory_type()
        peripheral = factory.create(config, simulate=is_simulated)

        i2c_config = ObjectScanner.find_single_or_default(config, I2CBase)
        if i2c_config is not None and i2c_config.multiplexer_details is not None:
            self.register_i2c_configuration(peripheral.key, i2c_config)
        elif i2c_config is not None: # Onboard i2c
            self.device.validate_i2c_pins(i2c_config.name, i2c_config.channel, i2c_config.i2c_address.value, i2c_config.gpio_pin_sda, i2c_config.gpio_pin_scl)

        adc_config = ObjectScanner.find_single_or_default(config, AnalogBase)
        if adc_config is not None and adc_config.adc_details is not None:
            self.register_adc_configuration(peripheral.key, adc_config)

        pin_configurations = ObjectScanner.find_all(config, PinConfig)           

        if (pin_configurations is not None):
            for idx, pin_config in enumerate(pin_configurations):
                self._register_pin(peripheral.key, idx + 1, pin_config)              

        if peripheral_type == PeripheralType.Sensor:
            self.sensors.register(peripheral)
        elif peripheral_type == PeripheralType.Actuator:
            self.actuators.register(peripheral)
        elif peripheral_type == PeripheralType.Communication:
            self.communication_modules.register(peripheral) 
        else:
            raise Exception(f'Unsupported peripheral type: {peripheral_type}')


    def __init__(self,
            device: Optional[DeviceBase] = None,
            is_simulated:bool = False,     
            device_type:DeviceType = DeviceType.Unknown,      
            adapter_type:AdapterType = AdapterType.Unknown,
            peripherals:List[ConfigBase] = None
        ):
    
        self._lock = RLock()

        self.device = device
        self.simulated = is_simulated
        self.pin_configurations = []
        self.warnings = []
        self.device_type = device_type
        self.adapter_type = adapter_type
        self.sensors = CatalogCategory[Sensor]()
        self.actuators = CatalogCategory[Actuator]()
        self.communication_modules = CatalogCategory[Communication]()

        for peripheral_config in peripherals:
            if peripheral_config is None:
                continue

            if peripheral_config.peripheral_type == PeripheralType.Communication:
                self._register_peripheral(
                    peripheral_type=PeripheralType.Communication,                 
                    config=peripheral_config, 
                    factory_type=CommunicationFactory, 
                    is_simulated=is_simulated) 
                
            elif peripheral_config.peripheral_type == PeripheralType.Sensor:
                self._register_peripheral(
                    peripheral_type=PeripheralType.Sensor,                 
                    config=peripheral_config, 
                    factory_type=SensorFactory, 
                    is_simulated=is_simulated)
                
            elif peripheral_config.peripheral_type == PeripheralType.Actuator:
                self._register_peripheral(
                    peripheral_type=PeripheralType.Actuator,                 
                    config=peripheral_config, 
                    factory_type=ActuatorFactory, 
                    is_simulated=is_simulated)
            
        self.validate()

        
