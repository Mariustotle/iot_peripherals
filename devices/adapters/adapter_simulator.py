from typing import Optional
from peripherals.contracts.adapter_type import AdapterType
from peripherals.devices.adapters.adapter_base import AdapterBase
from peripherals.devices.device_feature import DeviceFeature


class AdapterSimulator(AdapterBase):

    i2c_enabled:bool = None
    i2c_supported:bool = None
    uart_enabled:bool = None
    uart_supported:bool = None
    spi_enabled:bool = None
    spi_supported:bool = None
    pwm_enabled:bool = None
    pwm_supported:bool = None


    def __init__(self, adapter_type:AdapterType, i2c_enabled:bool = True, i2c_supported:bool = True, uart_enabled:bool = True, uart_supported:bool = True, spi_enabled:bool = True, spi_supported:bool = True, pwm_enabled:bool = True, pwm_supported:bool = True):
        super().__init__(adapter_type, True)

        self.i2c_supported = i2c_supported
        self.i2c_enabled = i2c_enabled
        self.uart_supported = uart_supported
        self.uart_enabled = uart_enabled
        self.spi_supported = spi_supported
        self.spi_enabled = spi_enabled
        self.pwm_supported = pwm_supported
        self.pwm_enabled = pwm_enabled

    # --------------------------------------------------------
    # Feature Builders
    # --------------------------------------------------------

    def build_i2c_feature(self, name:Optional[str] = None) -> 'DeviceFeature':
        return DeviceFeature.create("I2C", self.i2c_supported, self.i2c_enabled)

    def build_uart_feature(self, name:Optional[str] = None) -> 'DeviceFeature':
        return DeviceFeature.create("I2C", self.uart_supported, self.uart_enabled)

    def build_spi_feature(self, name:Optional[str] = None) -> 'DeviceFeature':
        return DeviceFeature.create("I2C", self.spi_supported, self.spi_enabled)

    def build_pwm_feature(self, name:Optional[str] = None) -> 'DeviceFeature':
        return DeviceFeature.create("I2C", self.pwm_supported, self.pwm_enabled)