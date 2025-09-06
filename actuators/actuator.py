from abc import ABC

from peripherals.actuators.actuator_types import ActuatorType

class Actuator(ABC):   
    actuator_type: ActuatorType = None
    device_name: str = None
    driver_name:str = None
    
    def __init__(self, actuator_type:ActuatorType, device_name:str, driver_name:str):
        self.actuator_type = actuator_type
        self.device_name = device_name
        self.driver_name = driver_name
