from peripherals.actuators.actuator_types import ActuatorType
from peripherals.peripheral import Peripheral
from peripherals.peripheral_type import PeripheralType

class Actuator(Peripheral):   
    actuator_type: ActuatorType = None
    driver_name:str = None
    
    def __init__(self, actuator_type:ActuatorType, name:str, driver_name:str):        
        super().__init__(PeripheralType.Actuator, name)

        self.actuator_type = actuator_type
        self.driver_name = driver_name
