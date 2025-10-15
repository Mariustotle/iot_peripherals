import os
import psutil
import platform
import time
import socket
import subprocess
from typing import Dict, Any, List, Optional

from peripherals.devices.diagnostic_base import DeviceDiagnosticsBase


class RaspberryPiDiagnostics(DeviceDiagnosticsBase):
    """Diagnostics implementation that adapts automatically to Raspberry Pi 3, 4, or 5."""

    def __init__(self):
        self._boot_time = psutil.boot_time()
        self.pi_model = self._detect_pi_model()

    # === Identification ===
    def _detect_pi_model(self) -> str:
        try:
            if os.path.exists("/proc/device-tree/model"):
                with open("/proc/device-tree/model", "r") as f:
                    model = f.read().strip()
                    if "Raspberry Pi 5" in model:
                        return "Raspberry Pi 5"
                    elif "Raspberry Pi 4" in model:
                        return "Raspberry Pi 4"
                    elif "Raspberry Pi 3" in model:
                        return "Raspberry Pi 3"
                    return model
            else:
                return platform.uname().machine
        except Exception:
            return "Unknown Raspberry Pi"

    def device_name(self):
        return self.pi_model

    def firmware_version(self):
        return platform.platform()

    def uptime(self):
        return round(time.time() - self._boot_time, 1)

    # === Hardware Status ===
    def cpu_usage(self):
        return psutil.cpu_percent(interval=0.5)

    def memory_usage(self):
        mem = psutil.virtual_memory()
        return {
            "total": mem.total,
            "used": mem.used,
            "free": mem.available,
            "percent": mem.percent,
        }

    def temperature(self) -> Optional[float]:
        """
        Attempts to detect temperature depending on Pi version:
        - Pi 3/4: /sys/class/thermal/thermal_zone0/temp
        - Pi 5:   /sys/devices/platform/cpu-thermal/thermal_zone*/temp
        """
        candidates = [
            "/sys/class/thermal/thermal_zone0/temp",
            "/sys/devices/platform/cpu-thermal/thermal_zone0/temp",
        ]
        for path in candidates:
            if os.path.exists(path):
                try:
                    with open(path, "r") as f:
                        return float(f.read()) / 1000.0
                except Exception:
                    continue
        return None

    def voltage_levels(self) -> Optional[Dict[str, float]]:
        """
        Tries to read voltage info if available (mostly Pi 5, optional Pi 4).
        Requires 'vcgencmd' tool (usually installed on Raspberry Pi OS).
        """
        voltage_data = {}
        try:
            result = subprocess.check_output(["vcgencmd", "measure_volts"], stderr=subprocess.DEVNULL)
            # Example output: "volt=0.8625V"
            for line in result.decode().splitlines():
                if "volt=" in line:
                    voltage_data["core"] = float(line.split("=")[1].replace("V", ""))
        except Exception:
            pass
        return voltage_data if voltage_data else None

    def available_gpio_pins(self) -> List[int]:
        """
        Returns GPIO pin range depending on model.
        All models have 40 pins, but usable pins differ slightly.
        """
        if "Pi 3" in self.pi_model:
            return list(range(2, 28))  # Broadcom GPIOs
        elif "Pi 4" in self.pi_model:
            return list(range(2, 28))
        elif "Pi 5" in self.pi_model:
            return list(range(2, 28))  # same layout but PCIe/GPIO shared
        else:
            return []

    # === Connectivity ===
    def network_status(self) -> Dict[str, Any]:
        try:
            ip = socket.gethostbyname(socket.gethostname())
            connected = True
        except socket.error:
            ip = None
            connected = False
        return {"status": "Online" if connected else "Offline", "ip": ip}

    def connected_peripherals(self) -> List[str]:
        try:
            output = subprocess.check_output(["lsusb"]).decode("utf-8").strip().splitlines()
            return [line.split()[-1] for line in output]
        except Exception:
            return []

    # === Health Summary ===
    def health_summary(self) -> Dict[str, Any]:
        """Aggregate metrics dynamically using base helper pattern."""
        base = super().health_summary()
        base["device_name"] = self.device_name()
        base["firmware_version"] = self.firmware_version()
        base["uptime"] = self.uptime()
        base["cpu_usage"] = self.cpu_usage()
        base["temperature"] = self.temperature()
        base["memory_usage"] = self.memory_usage()
        base["network"] = self.network_status()
        base["peripherals"] = self.connected_peripherals()
        voltage = self.voltage_levels()
        if voltage:
            base["voltage"] = voltage
        return base

    # === System Control ===
    def reboot(self):
        try:
            subprocess.call(["sudo", "reboot"])
            return True
        except Exception:
            return False

    def safe_shutdown(self):
        try:
            subprocess.call(["sudo", "shutdown", "-h", "now"])
            return True
        except Exception:
            return False
