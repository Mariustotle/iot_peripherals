
from peripherals.communication.communication_type import CommunicationType
from peripherals.peripheral import Peripheral
from peripherals.peripheral_type import PeripheralType

class Communication(Peripheral):   
    communication_type: CommunicationType = None
    driver_name:str = None
    
    def __init__(self, communication_type:CommunicationType, name:str, driver_name:str):        
        super().__init__(PeripheralType.Actuator, name)

        self.communication_type = communication_type
        self.driver_name = driver_name
