import os
from peripherals.contracts.device_type import DeviceType
from peripherals.contracts.pins.pin_types import PinType
from peripherals.devices.device_base import DeviceBase
from peripherals.devices.device_feature import DeviceFeature


class RaspberryPi3(DeviceBase):
    def __init__(self):
        super().__init__(DeviceType.RaspberryPi3, PinType.DIGITAL)
        self.configure_available_pins()

    # --------------------------------------------------------
    # Feature Detection Helpers
    # --------------------------------------------------------

    def _is_feature_enabled_in_config(self, keyword: str) -> bool:
        """
        Check /boot/config.txt or /boot/firmware/config.txt for enabled overlays.
        Example: 'dtparam=i2c_arm=on' or 'dtparam=spi=on'
        """
        possible_files = ["/boot/config.txt", "/boot/firmware/config.txt"]
        for file_path in possible_files:
            if not os.path.exists(file_path):
                continue
            with open(file_path, "r") as f:
                for line in f:
                    if keyword in line and "off" not in line:
                        return True
        return False

    def _is_device_present(self, device_hint: str) -> bool:
        """Check /dev entries for presence of a device."""
        for entry in os.listdir("/dev"):
            if device_hint in entry:
                return True
        return False

    # --------------------------------------------------------
    # Feature Builders
    # --------------------------------------------------------

    def _build_i2c_feature(self) -> 'DeviceFeature':
        is_supported = True
        is_enabled = (
            self._is_feature_enabled_in_config("i2c_arm=on") or
            self._is_device_present("i2c-")
        )
        return DeviceFeature.create("I2C", is_supported, is_enabled)

    def _build_uart_feature(self) -> 'DeviceFeature':
        is_supported = True
        is_enabled = (
            self._is_feature_enabled_in_config("enable_uart=1") or
            self._is_device_present("ttyAMA") or
            self._is_device_present("serial")
        )
        return DeviceFeature.create("UART", is_supported, is_enabled)

    def _build_spi_feature(self) -> 'DeviceFeature':
        is_supported = True
        is_enabled = (
            self._is_feature_enabled_in_config("spi=on") or
            self._is_device_present("spidev")
        )
        return DeviceFeature.create("SPI", is_supported, is_enabled)

    def _build_pwm_feature(self) -> 'DeviceFeature':
        is_supported = True
        # PWM often requires no explicit config; test /sys/class/pwm
        is_enabled = os.path.exists("/sys/class/pwm")
        return DeviceFeature.create("PWM", is_supported, is_enabled)

    # --------------------------------------------------------
    # Pin Configuration
    # --------------------------------------------------------

    def configure_available_pins(self):
        """Builds all GPIO feature mappings for Raspberry Pi 3."""
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
