


from peripherals.contracts.device_type import DeviceType
from peripherals.devices.diagnostic_base import DeviceDiagnosticsBase

class DeviceDiagnosticFactory:

    @staticmethod
    def create_device(device_type: DeviceType, simulate:bool) -> DeviceDiagnosticsBase:
        """Factory method to create device diagnostics instances."""
        device_type = device_type.lower()
        if simulate:
            from peripherals.devices.device_simulator import DeviceSimulator
            return DeviceSimulator()

        if device_type in (DeviceType.RaspberryPi3, DeviceType.RaspberryPi4, DeviceType.RaspberryPi5):
            from peripherals.devices.rapberry_pi import RaspberryPiDiagnostics
            return RaspberryPiDiagnostics()

        else:
            raise ValueError(f"Unsupported device type: {device_type}")