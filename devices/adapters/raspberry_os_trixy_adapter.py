

import os
from peripherals.contracts.adapter_type import AdapterType
from peripherals.devices.adapters.adapter_base import AdapterBase
from peripherals.devices.device_feature import DeviceFeature

class RaspberryOSTrixyAdapter(AdapterBase):
    """
    Adapter implementation for Raspberry Pi OS Bookworm and Trixie (2023+).
    Detects and enables features dynamically from /sys and /dev interfaces.
    """

    def __init__(self, adapter_type: AdapterType):
        super().__init__(adapter_type, simulated=False)

    # --------------------------------------------------------
    # I2C
    # --------------------------------------------------------
    def build_i2c_feature(self, instance: int = 0) -> 'DeviceFeature':
        name = f"I2C-{instance}"
        dev_path = f"/dev/i2c-{instance}"

        supported = os.path.exists(dev_path)
        enabled = supported and self._is_module_loaded("i2c_bcm2835")
        return DeviceFeature.create(name, supported, enabled)

    # --------------------------------------------------------
    # UART
    # --------------------------------------------------------
    def build_uart_feature(self, instance: int = 0) -> 'DeviceFeature':
        name = f"UART-{instance}"

        # Default serial port for Pi OS (Bookworm/Trixie)
        uart_devices = ["/dev/serial0", "/dev/ttyAMA0", "/dev/ttyS0"]
        supported = any(os.path.exists(dev) for dev in uart_devices)

        # On modern Pi OS, serial console may be disabled or linked to Bluetooth
        enabled = supported and not self._is_console_on_uart()
        return DeviceFeature.create(name, supported, enabled)

    # --------------------------------------------------------
    # SPI
    # --------------------------------------------------------
    def build_spi_feature(self, instance: int = 0) -> 'DeviceFeature':
        name = f"SPI-{instance}"
        dev_path = f"/dev/spidev0.{instance}"

        supported = os.path.exists(dev_path)
        enabled = supported and self._is_module_loaded("spidev")
        return DeviceFeature.create(name, supported, enabled)

    # --------------------------------------------------------
    # PWM
    # --------------------------------------------------------
    def build_pwm_feature(self, instance: int = 0) -> 'DeviceFeature':
        name = f"PWM-{instance}"

        # Detect if the /sys/class/pwm directory exists
        pwm_dir = "/sys/class/pwm"
        supported = os.path.exists(pwm_dir) and any("pwmchip" in d for d in os.listdir(pwm_dir))

        # Enabled if any exported PWM channel is present
        enabled = supported and any("pwm" in d for d in os.listdir(pwm_dir))
        return DeviceFeature.create(name, supported, enabled)

    # --------------------------------------------------------
    # Helper methods
    # --------------------------------------------------------
    def _is_module_loaded(self, module: str) -> bool:
        """Check if a kernel module is loaded."""
        try:
            with open("/proc/modules") as f:
                return any(line.startswith(module) for line in f)
        except Exception:
            return False

    def _is_console_on_uart(self) -> bool:
        """
        Check if the serial console is using the UART (common conflict).
        On modern Pi OS, 'enable_uart=1' must be in /boot/firmware/config.txt
        for it to be enabled.
        """
        try:
            with open("/boot/firmware/config.txt") as f:
                for line in f:
                    if line.strip().startswith("enable_uart"):
                        return line.strip().endswith("=1")
        except FileNotFoundError:
            pass
        return False
    