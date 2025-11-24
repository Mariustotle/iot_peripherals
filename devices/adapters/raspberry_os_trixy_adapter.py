from typing import List, Tuple
from peripherals.contracts.adapter_type import AdapterType
from peripherals.devices.adapters.adapter_base import AdapterBase
from peripherals.devices.device_feature import DeviceFeature

import os
import smbus2

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
    

    def validate_i2c(self, name: str, channel: int, i2c_address: int) -> Tuple[List[str], List[str]]:
        debug = []
        errors = []

        debug.append(f"Adapter-level I2C validation for [{name}]")
        debug.append(f"  • Channel        : {channel}")
        debug.append(f"  • I2C Address    : 0x{i2c_address:02X} ({i2c_address})")

        # --------------------------------------------------------
        # 1. Check if device file /dev/i2c-X exists
        # --------------------------------------------------------
        bus_path = f"/dev/i2c-{channel}"
        if not os.path.exists(bus_path):
            errors.append(f"  ✖ ERROR: I2C bus device '{bus_path}' does NOT exist.")
            errors.append("     → I2C disabled, wrong bus, or dtoverlay misconfigured.")
            return debug, errors

        # --------------------------------------------------------
        # 2. Attempt to open the bus
        # --------------------------------------------------------
        try:
            bus = smbus2.SMBus(channel)
            debug.append("  ✔ Opened I2C bus successfully")
        except Exception as ex:
            errors.append("  ✖ ERROR: Failed to open I2C bus.")
            errors.append(f"     System error: {ex}")
            return debug, errors

        # --------------------------------------------------------
        # 3. Test connectivity to the I2C address
        # --------------------------------------------------------
        try:
            # This performs an actual read attempt and checks for an ACK.
            # Nearly all I2C sensors will respond to reading register 0x00.
            bus.read_byte(i2c_address)
            debug.append(f"  ✔ Device at 0x{i2c_address:02X} responded (ACK received).")

        except OSError as ex:
            errno_val = ex.errno

            if errno_val == 121:  # Remote I/O error (no ACK)
                errors.append(f"  ✖ ERROR: Device at 0x{i2c_address:02X} did NOT respond (no ACK).")
                errors.append("     → Most common causes:")
                errors.append("       • Wrong SDA/SCL pins")
                errors.append("       • Wrong I2C address")
                errors.append("       • Sensor not powered")
                errors.append("       • Faulty jumper wire")
                errors.append(f"     System error: {ex}")

            elif errno_val == 5:  # I/O error (bus physically unusable)
                errors.append(f"  ✖ ERROR: Severe I/O error talking to device at 0x{i2c_address:02X}.")
                errors.append("     → SDA/SCL likely shorted, reversed, or floating.")
                errors.append("       This error means the hardware lines failed electrically.")
                errors.append(f"     System error: {ex}")

            else:
                errors.append(f"  ✖ ERROR: Unknown I2C communication failure for device 0x{i2c_address:02X}.")
                errors.append(f"     System error: {ex}")

        except Exception as ex:
            errors.append(f"  ✖ ERROR: Unexpected failure testing device at 0x{i2c_address:02X}.")
            errors.append(f"     System error: {ex}")

        # Clean up bus handle
        try:
            bus.close()
        except:
            pass

        return debug, errors
