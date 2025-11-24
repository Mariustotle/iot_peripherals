from typing import List, Optional, Tuple
from peripherals.contracts.adapter_type import AdapterType
from peripherals.contracts.simulator.simulator_config import SimulatorConfig
from peripherals.devices.adapters.adapter_base import AdapterBase
from peripherals.devices.device_feature import DeviceFeature


class AdapterSimulator(AdapterBase):
    config:SimulatorConfig = None
    features:List[DeviceFeature] = None

    def __init__(self, adapter_type:AdapterType, config:SimulatorConfig):
        super().__init__(adapter_type, True)

        self.config = config
        self.features = []

    def _get_feature_name(self, type:str, instance:int = 0):
        return  f"{type}-{instance}-sim"    

    # --------------------------------------------------------
    # Feature Builders
    # --------------------------------------------------------

    def build_i2c_feature(self, instance:int = 0) -> 'DeviceFeature':
        feature = next((item for item in self.config.i2c if item.instance == instance), None)
        name = self._get_feature_name("I2C", instance)
        device_feature:DeviceFeature = None

        if feature is not None:
            device_feature = DeviceFeature.create(name, feature.supported, feature.enabled)        
        else:
            device_feature = DeviceFeature.create(name, self.config.default_supported_state, self.config.default_enabled_state)

        self.features.append(device_feature)
        return device_feature
    

    def build_uart_feature(self, instance:int = 0) -> 'DeviceFeature':
        feature = next((item for item in self.config.uart if item.instance == instance), None)
        name = self._get_feature_name("UART", instance)
        device_feature:DeviceFeature = None

        if feature is not None:
            device_feature = DeviceFeature.create(name, feature.supported, feature.enabled)        
        else:
            device_feature = DeviceFeature.create(name, self.config.default_supported_state, self.config.default_enabled_state)
        
        self.features.append(device_feature)
        return device_feature
    

    def build_spi_feature(self, instance:int = 0) -> 'DeviceFeature':
        feature = next((item for item in self.config.spi if item.instance == instance), None)
        name = self._get_feature_name("SPI", instance)
        device_feature:DeviceFeature = None

        if feature is not None:
            device_feature =  DeviceFeature.create(name, feature.supported, feature.enabled)        
        else:
            device_feature =  DeviceFeature.create(name, self.config.default_supported_state, self.config.default_enabled_state)
        
        self.features.append(device_feature)
        return device_feature

    def build_pwm_feature(self, instance:int = 0) -> 'DeviceFeature':
        feature = next((item for item in self.config.pwm if item.instance == instance), None)
        name = self._get_feature_name("PWM", instance)
        device_feature:DeviceFeature = None

        if feature is not None:
            device_feature =  DeviceFeature.create(name, feature.supported, feature.enabled)        
        else:
            device_feature =  DeviceFeature.create(name, self.config.default_supported_state, self.config.default_enabled_state)

        self.features.append(device_feature)
        return device_feature

    def validate_i2c(self, name:str, channel:int, i2c_address:int) -> Tuple[List[str], List[str]]:
        debug = []
        errors = []

        feature_name = self._get_feature_name("I2C", channel)

        found_feature = next((item for item in self.features if item.name == feature_name), None)

        if not found_feature:
            errors.append(f'  ✖ The required I2C feature [{feature_name}] on channel [{channel}] have not been configured on this device.')


        if found_feature and not found_feature.supported:
            errors.append(f'  ✖ The required I2C feature [{feature_name}] on channel [{channel}] is not supported.')

        if found_feature and not found_feature.enabled:
            errors.append(f'  ✖ The required I2C feature [{feature_name}] on channel [{channel}] is supported but not currently enabled.')
            
        if len(errors) == 0:
            debug.append(f'  ✔ The required I2C feature [{feature_name}] on channel [{channel}] exists and is enabled.')

        return (debug, errors)