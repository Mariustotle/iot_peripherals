import os
from peripherals.contracts.device_type import DeviceType
from peripherals.contracts.pins.pin_types import PinType
from peripherals.devices.adapters.adapter_base import AdapterBase
from peripherals.devices.device_base import DeviceBase
from peripherals.devices.device_feature import DeviceFeature


class RaspberryPi4(DeviceBase):

    def __init__(self, adapter:AdapterBase):
        super().__init__(DeviceType.RaspberryPi4, adapter, PinType.DIGITAL)
        self.configure_available_pins()

    # --------------------------------------------------------
    # Pin Configuration
    # --------------------------------------------------------

    def configure_available_pins(self):
        """Configures GPIO, I2C, SPI, UART, and PWM pins for Raspberry Pi 4."""

        # --- I2C ---
        i2c_feature = self.adapter.build_i2c_feature()
        self.add_pin(2, 3, PinType.I2C_SDA, i2c_feature)  # GPIO2 (SDA1)
        self.add_pin(3, 5, PinType.I2C_SCL, i2c_feature)  # GPIO3 (SCL1)
        # Additional I2C bus on GPIO0/1 possible, but not active by default

        # --- UART ---
        uart_feature = self.adapter.build_uart_feature()
        self.add_pin(14, 8, PinType.UART_TX, uart_feature)  # GPIO14 TXD0
        self.add_pin(15, 10, PinType.UART_RX, uart_feature) # GPIO15 RXD0

        # --- SPI ---
        spi_feature = self.adapter.build_spi_feature()
        self.add_pin(7, 26, PinType.SPI_CE1, spi_feature)
        self.add_pin(8, 24, PinType.SPI_CE0, spi_feature)
        self.add_pin(9, 21, PinType.SPI_MISO, spi_feature)
        self.add_pin(10, 19, PinType.SPI_MOSI, spi_feature)
        self.add_pin(11, 23, PinType.SPI_SCLK, spi_feature)
        # GPIO16–21 can serve as SPI1 if overlay is enabled

        # --- PWM ---
        pwm_feature = self.adapter.build_pwm_feature()
        self.add_pin(12, 32, PinType.PWM_0, pwm_feature)  # GPIO12
        self.add_pin(13, 33, PinType.PWM_1, pwm_feature)  # GPIO13
        self.add_pin(18, 12, PinType.PWM_0, pwm_feature)  # GPIO18
        self.add_pin(19, 35, PinType.PWM_1, pwm_feature)  # GPIO19

        # --- Standard GPIO ---
        self.add_pin(4, 7)     # GPIO4
        self.add_pin(17, 11)   # GPIO17
        self.add_pin(27, 13)   # GPIO27
        self.add_pin(22, 15)   # GPIO22
        self.add_pin(23, 16)   # GPIO23
        self.add_pin(24, 18)   # GPIO24
        self.add_pin(25, 22)   # GPIO25
        self.add_pin(5, 29)    # GPIO5
        self.add_pin(6, 31)    # GPIO6
        self.add_pin(16, 36)   # GPIO16
        self.add_pin(20, 38)   # GPIO20
        self.add_pin(21, 40)   # GPIO21
