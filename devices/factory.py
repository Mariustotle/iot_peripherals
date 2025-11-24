from peripherals.contracts.adapter_type import AdapterType
from peripherals.contracts.device_type import DeviceType
from peripherals.contracts.pins.pin_types import PinType
from peripherals.contracts.simulator.simulator_config import SimulatorConfig
from peripherals.devices.adapters.adapter_base import AdapterBase
from peripherals.devices.adapters.adapter_simulator import AdapterSimulator

from peripherals.devices.device_base import DeviceBase
from peripherals.devices.raspberry_pi_3 import RaspberryPi3
from peripherals.devices.raspberry_pi_4 import RaspberryPi4


class DeviceFactory:

    @staticmethod
    def _create_adapter(adapter_type:AdapterType, sim_config:SimulatorConfig) -> AdapterBase:    
        if sim_config.enabled:
            return AdapterSimulator(adapter_type, config=sim_config)
        
        if (adapter_type == AdapterType.RaspberryOSTrixy):
            from peripherals.devices.adapters.raspberry_os_trixy_adapter import RaspberryOSTrixyAdapter
            return RaspberryOSTrixyAdapter(adapter_type)
        
        else:
            raise Exception(f'Not able to create adapter for [{adapter_type.name}] it has not yet been configured.')


    @staticmethod
    def create_device(device_type: DeviceType, adapter_type:AdapterType, simulate:bool) -> DeviceBase:
        adapter = DeviceFactory._create_adapter(adapter_type, simulate)

        if device_type == DeviceType.RaspberryPi3:
            return RaspberryPi3(device_type=device_type, adapter=adapter, default_pin_type=PinType.DIGITAL)
        elif device_type == DeviceType.RaspberryPi4:
            return RaspberryPi4(device_type=device_type, adapter=adapter, default_pin_type=PinType.DIGITAL)

        else:
            raise ValueError(f"Unsupported device type: {device_type}")