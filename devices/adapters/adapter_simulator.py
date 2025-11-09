from typing import Optional
from peripherals.contracts.adapter_type import AdapterType
from peripherals.contracts.simulator.simulator_config import SimulatorConfig
from peripherals.devices.adapters.adapter_base import AdapterBase
from peripherals.devices.device_feature import DeviceFeature


class AdapterSimulator(AdapterBase):
    config:SimulatorConfig = None

    def __init__(self, adapter_type:AdapterType, config:SimulatorConfig):
        super().__init__(adapter_type, True)

        self.config = config

    # --------------------------------------------------------
    # Feature Builders
    # --------------------------------------------------------

    def build_i2c_feature(self, instance:int = 0) -> 'DeviceFeature':
        feature = next((item for item in self.config.i2c if item.instance == instance), None)
        name = f"I2C-{instance}-sim"

        if feature is not None:
            return DeviceFeature.create(name, feature.supported, feature.enabled)        
        else:
            return DeviceFeature.create(name, self.config.default_supported_state, self.config.default_enabled_state)

    def build_uart_feature(self, instance:int = 0) -> 'DeviceFeature':
        feature = next((item for item in self.config.uart if item.instance == instance), None)
        name = f"UART-{instance}-sim"

        if feature is not None:
            return DeviceFeature.create(name, feature.supported, feature.enabled)        
        else:
            return DeviceFeature.create(name, self.config.default_supported_state, self.config.default_enabled_state)

    def build_spi_feature(self, instance:int = 0) -> 'DeviceFeature':
        feature = next((item for item in self.config.spi if item.instance == instance), None)
        name = f"SPI-{instance}-sim"

        if feature is not None:
            return DeviceFeature.create(name, feature.supported, feature.enabled)        
        else:
            return DeviceFeature.create(name, self.config.default_supported_state, self.config.default_enabled_state)

    def build_pwm_feature(self, instance:int = 0) -> 'DeviceFeature':
        feature = next((item for item in self.config.pwm if item.instance == instance), None)
        name = f"PWM-{instance}-sim"

        if feature is not None:
            return DeviceFeature.create(name, feature.supported, feature.enabled)        
        else:
            return DeviceFeature.create(name, self.config.default_supported_state, self.config.default_enabled_state)