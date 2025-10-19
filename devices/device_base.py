from typing import Optional

from peripherals.contracts.device_type import DeviceType
from peripherals.contracts.pins.pin_number import PinNumber
from peripherals.contracts.pins.pin_details import PinDetails
from peripherals.contracts.pins.pin_types import PinType
from peripherals.devices.device_feature import DeviceFeature

class DeviceBase:
    device_type:DeviceType = None
    default_pin_type:PinType = None
    available_pins:dict[PinNumber, PinDetails] = None

    i2c_feature:Optional[DeviceFeature] = None
    uart_feature:Optional[DeviceFeature] = None
    spi_feature:Optional[DeviceFeature] = None

    def _find_pin(self, gpio_number:Optional[int], board_number:Optional[int]) -> Optional[PinDetails]:
        if (not gpio_number and not board_number):
            raise Exception('You must provide either a gpio or board pin number.')
        
        found: PinDetails = None

        if gpio_number:
            found = next((k for k in self.available_pins if k.gpio_pin == gpio_number), None)

        if not found and board_number:
            found = next((k for k in self.available_pins if k.board_pin == board_number), None)

        if not found:
            msg = "\n".join(f" - Pin: GPIO=[{pin.gpio_pin}], BOARD=[{pin.board_pin}]" for pin in self.available_pins.keys)
            raise Exception(f'Unable to find available PIN (GPIO=[{gpio_number}], BOARD=[{board_number}]). Available pins on [{self.device_type.name}]: {msg}')

        return found


    def __init__(self, device_type:DeviceType, default_pin_type:PinType):
        self.device_type = device_type
        self.pin_default_type = default_pin_type
        self.available_pins: dict[PinNumber, PinDetails] = {}
        self.available_pins = self.configure_available_pins()


    def add_pin(self, gpio_number:Optional[int], board_number:Optional[int], standard_mode:Optional[PinType] = None, feature:Optional[DeviceFeature] = None, special_mode:Optional[PinType] = None):
        pin_number = PinNumber(gpio_pin=gpio_number, board_pin=board_number)
        
        found = self.available_pins.get(pin_number)

        if (not found):
            standard_mode = standard_mode if standard_mode else self.pin_default_type
            self.available_pins[pin_number] = PinDetails(standard_mode=standard_mode, special_mode=special_mode, feature=feature)

        else:
            raise Exception(f'[board_pin={board_number}/gpio_pin={gpio_number}] pin have already been added.')
        

    def configure_available_pins(self):
         raise Exception(f'Please override [configure_available_pins] in the base class.')
    

    def validate_pin(self, pin_type:PinType,  gpio_number:Optional[int], board_number:Optional[int]):
        device_pin = self._find_pin(gpio_number=gpio_number, board_number=board_number)        

        standard_pin = True if device_pin.feature == None or not device_pin.feature.enabled else False
        pin_supports_type:bool = True if device_pin.standard_mode == pin_type or device_pin.special_mode == pin_type else False
        pin_type_validated: bool = False

        if standard_pin:
            pin_type_validated = device_pin.standard_mode == pin_type
        elif(device_pin.feature):
            pin_type_validated = device_pin.special_mode == pin_type
        else:
            # In case of no feature either standard or special pin can be used
            pin_type_validated = pin_supports_type

        if not pin_supports_type:
            # Show other pins that support this type
            msg = "\n".join(f" - Pin: GPIO=[{key.gpio_pin}], BOARD=[{key.board_pin}]" for (key, value) in self.available_pins if value.standard_mode == pin_type or value.special_mode == pin_type)
            raise Exception(f'Unable to use pin (GPIO=[{gpio_number}], BOARD=[{board_number}]) the specified pin does not support [{pin_type.name}]. Other pins on [{self.device_type.name}] that support this type of pin is: {msg}')

        if not pin_type_validated:
            raise Exception(f'Pin (GPIO=[{gpio_number}], BOARD=[{board_number}]) has not been able to validate usage of [{pin_type.name}]. Standard=[{device_pin.standard_mode.name}], Special=[{device_pin.special_mode.name if device_pin.special_mode else 'N/A'}], feature=[{str(device_pin.feature)}]')

        return True # Validated
    
    '''
    

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

    '''
