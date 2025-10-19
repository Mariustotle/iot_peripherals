import random
import time
from typing import Dict, Any

from peripherals.devices.device_base import DeviceDiagnosticsBase


class DeviceSimulator(DeviceDiagnosticsBase):
    """Simulated device for development and testing."""

    def __init__(self):
        super().__init__()
        self.start_time = time.time()
        self._fake_peripherals = [
            "Simulated-TemperatureSensor",
            "Simulated-HumiditySensor",
            "Virtual-I2C-Module",
        ]

    def device_name(self): return "Simulated IoT Device"
    def firmware_version(self): return "SimOS 1.0.0"
    def uptime(self): return round(time.time() - self.start_time, 1)

    def cpu_usage(self): return round(random.uniform(1, 30), 1)
    def memory_usage(self): 
        used_percent = random.uniform(20, 70)
        return {"total": 1024*1024*512, "used": used_percent, "percent": used_percent}
    def temperature(self): return round(random.uniform(25.0, 45.0), 1)
    def available_gpio_pins(self): return list(range(2, 28))
    def network_status(self): 
        return {"status": "Online", "ip": f"192.168.0.{random.randint(2, 250)}"}
    def connected_peripherals(self): return random.sample(self._fake_peripherals, k=random.randint(1, len(self._fake_peripherals)))
    def run_diagnostics(self) -> Dict[str, Any]:
        return {
            "simulated_load_test": random.choice(["Pass", "Fail"]),
            "last_run": time.ctime(),
        }
