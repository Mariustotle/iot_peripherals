import os
from peripherals.contracts.device_type import DeviceType
from peripherals.contracts.pins.pin_types import PinType
from peripherals.devices.device_base import DeviceBase
from peripherals.devices.device_feature import DeviceFeature

class DeviceSimulator(DeviceBase):

    def __init__(self):
        super().__init__(DeviceType.RaspberryPi3, PinType.DIGITAL)
        self.configure_available_pins()


    # --------------------------------------------------------
    # Feature Builders
    # --------------------------------------------------------

    def _build_i2c_feature(self) -> 'DeviceFeature':
        is_supported = True
        is_enabled = True
        return DeviceFeature.create("I2C", is_supported, is_enabled)

    def _build_uart_feature(self) -> 'DeviceFeature':
        is_supported = True
        is_enabled = True
        return DeviceFeature.create("UART", is_supported, is_enabled)

    def _build_spi_feature(self) -> 'DeviceFeature':
        is_supported = True
        is_enabled = True
        return DeviceFeature.create("SPI", is_supported, is_enabled)

    def _build_pwm_feature(self) -> 'DeviceFeature':
        is_supported = True
        is_enabled = True
        return DeviceFeature.create("PWM", is_supported, is_enabled)

    # --------------------------------------------------------
    # Pin Configuration
    # --------------------------------------------------------

    def configure_available_pins(self):

        # I2C
        i2c_feature = self._build_i2c_feature()
        self.add_pin(2, 3, PinType.I2C_SDA, i2c_feature)
        self.add_pin(3, 5, PinType.I2C_SCL, i2c_feature)

        # UART
        uart_feature = self._build_uart_feature()
        self.add_pin(14, 8, PinType.UART_TX, uart_feature)
        self.add_pin(15, 10, PinType.UART_RX, uart_feature)

        # SPI
        spi_feature = self._build_spi_feature()
        self.add_pin(9, 21, PinType.SPI_MISO, spi_feature)
        self.add_pin(10, 19, PinType.SPI_MOSI, spi_feature)
        self.add_pin(11, 23, PinType.SPI_SCLK, spi_feature)
        self.add_pin(8, 24, PinType.SPI_CE0, spi_feature)
        self.add_pin(7, 26, PinType.SPI_CE1, spi_feature)

        # PWM
        pwm_feature = self._build_pwm_feature()
        self.add_pin(12, 32, PinType.PWM_0, pwm_feature)
        self.add_pin(13, 33, PinType.PWM_1, pwm_feature)
        self.add_pin(18, 12, PinType.PWM_0, pwm_feature)

        # Standard GPIO (no special mode, no feature object)
        self.add_pin(4, 7)
        self.add_pin(25, 22)
