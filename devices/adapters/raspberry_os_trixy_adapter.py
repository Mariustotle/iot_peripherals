

import os
from typing import Optional
from peripherals.devices.adapters.adapter_base import AdapterBase
from peripherals.devices.device_feature import DeviceFeature

class RaspberryOSTrixyAdapter(AdapterBase):


    # --------------------------------------------------------
    # Feature Detection Helpers
    # --------------------------------------------------------

    def is_feature_enabled_in_config(self, keyword: str) -> bool:
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

    def is_device_present(self, device_hint: str) -> bool:
        """Check /dev entries for presence of a device."""
        for entry in os.listdir("/dev"):
            if device_hint in entry:
                return True
        return False

    # --------------------------------------------------------
    # Feature Builders
    # --------------------------------------------------------

    def build_i2c_feature(self, name:Optional[str] = None) -> 'DeviceFeature':
        is_supported = True
        is_enabled = (
            self._is_feature_enabled_in_config("i2c_arm=on") or
            self._is_device_present("i2c-")
        )
        return DeviceFeature.create("I2C", is_supported, is_enabled)

    def build_uart_feature(self, name:Optional[str] = None) -> 'DeviceFeature':
        is_supported = True
        is_enabled = (
            self._is_feature_enabled_in_config("enable_uart=1") or
            self._is_device_present("ttyAMA") or
            self._is_device_present("serial")
        )
        return DeviceFeature.create("UART", is_supported, is_enabled)

    def build_spi_feature(self, name:Optional[str] = None) -> 'DeviceFeature':
        is_supported = True
        is_enabled = (
            self._is_feature_enabled_in_config("spi=on") or
            self._is_device_present("spidev")
        )
        return DeviceFeature.create("SPI", is_supported, is_enabled)

    def build_pwm_feature(self, name:Optional[str] = None) -> 'DeviceFeature':
        is_supported = True
        # PWM often requires no explicit config; test /sys/class/pwm
        is_enabled = os.path.exists("/sys/class/pwm")
        return DeviceFeature.create("PWM", is_supported, is_enabled)