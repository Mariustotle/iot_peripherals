


from peripherals.contracts.adapter_type import AdapterType
from peripherals.contracts.device_type import DeviceType
from peripherals.devices.adapters.adapter_base import AdapterBase
from peripherals.devices.adapters.adapter_simulator import AdapterSimulator
from peripherals.devices.adapters.raspberry_os_trixy_adapter import RaspberryOSTrixyAdapter
from peripherals.devices.device_base import DeviceBase
from peripherals.devices.raspberry_pi_3 import RaspberryPi3
from peripherals.devices.raspberry_pi_4 import RaspberryPi4

class DeviceFactory:

    @staticmethod
    def _create_adapter(adapter_type:AdapterType, simulate:bool) -> AdapterBase:    
        if simulate:
            return AdapterSimulator(adapter_type)
        
        if (adapter_type == AdapterType.RaspberryOSTrixy):
            return RaspberryOSTrixyAdapter(adapter_type)
        
        else:
            raise Exception(f'Not able to create adapter for [{adapter_type.name}] it has not yet been configured.')


    @staticmethod
    def create_device(device_type: DeviceType, adapter_type:AdapterType, simulate:bool) -> DeviceBase:
        adapter = DeviceFactory._create_adapter(adapter_type, simulate)

        if device_type == DeviceType.RaspberryPi3:
            return RaspberryPi3(adapter)
        
        if device_type == DeviceType.RaspberryPi4:
            return RaspberryPi4(adapter)

        else:
            raise ValueError(f"Unsupported device type: {device_type}")