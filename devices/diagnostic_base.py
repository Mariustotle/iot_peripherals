from typing import Dict, Any, List, Optional
import inspect


class DeviceDiagnosticsBase:
    """Flexible base class for IoT device health and diagnostics."""

    # === Identification (optional overrides) ===
    def device_name(self) -> Optional[str]: return None
    def firmware_version(self) -> Optional[str]: return None
    def uptime(self) -> Optional[float]: return None

    # === Hardware Status ===
    def cpu_usage(self) -> Optional[float]: return None
    def memory_usage(self) -> Optional[Dict[str, float]]: return None
    def temperature(self) -> Optional[float]: return None
    def available_gpio_pins(self) -> Optional[List[int]]: return None

    # === Connectivity ===
    def network_status(self) -> Optional[Dict[str, Any]]: return None
    def connected_peripherals(self) -> Optional[List[str]]: return None

    # === Diagnostics ===
    def run_diagnostics(self) -> Optional[Dict[str, Any]]: return None

    # === System Control ===
    def reboot(self) -> bool: return False
    def safe_shutdown(self) -> bool: return False

    # === Health Summary ===
    def health_summary(self) -> Dict[str, Any]:
        """
        Builds a summary by introspecting available methods.
        Only includes implemented (non-None) metrics.
        """
        summary = {}
        method_map = {
            "device_name": self.device_name,
            "firmware_version": self.firmware_version,
            "uptime": self.uptime,
            "cpu_usage": self.cpu_usage,
            "temperature": self.temperature,
            "memory_usage": self.memory_usage,
            "network": self.network_status,
            "peripherals": self.connected_peripherals,
        }

        for key, method in method_map.items():
            try:
                # Check if overridden (not inherited directly)
                base_method = getattr(DeviceDiagnosticsBase, method.__name__, None)
                if base_method and inspect.unwrap(method) == base_method:
                    continue  # Skip if not overridden

                result = method()
                if result not in [None, {}, [], ""]:
                    summary[key] = result
            except Exception as ex:
                summary[key] = f"Error: {ex.__class__.__name__}"

        return summary

    # === Default Console Overview ===
    def health_overview(self) -> None:
        summary = self.health_summary()

        print("\n========== DEVICE HEALTH OVERVIEW ==========")
        for key, value in summary.items():
            if isinstance(value, dict):
                if key == "memory_usage":
                    print(f"Memory Used: {value.get('percent', '?')}%")
                elif key == "network":
                    print(f"Network: {value.get('status', '?')} ({value.get('ip', '-')})")
                else:
                    print(f"{key.replace('_', ' ').title()}: {value}")
            elif isinstance(value, list):
                print(f"{key.replace('_', ' ').title()}: {', '.join(value)}")
            else:
                print(f"{key.replace('_', ' ').title()}: {value}")
        print("============================================\n")
