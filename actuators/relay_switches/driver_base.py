from abc import abstractmethod

from peripherals.actuators.action_decorator import action
from peripherals.actuators.actuator import Actuator
from peripherals.actuators.actuator_types import ActuatorType
from peripherals.actuators.relay_switches.config import RelayConfig
from peripherals.actuators.relay_switches.relay_drivers import RelayDrivers
from peripherals.contracts.on_off_status import OnOffStatus

class RelayDriverBase(Actuator):    
    config:RelayConfig = None
    simulated:bool = None
    relay_pin:int = None
    relay_status:OnOffStatus = None         # The on/off status of the relay
    power_status:OnOffStatus = None         # Whether the power is on (based on relay status and default state)
    
    def __init__(self, config:RelayConfig, simulated:bool = False):
        driver = config.driver if config.driver is not None else RelayDrivers.Default
        driver_name = driver.value if not simulated else 'N/A - Simulated'

        super().__init__(ActuatorType.Relay, config.name, driver_name, status=config.default_power_status)
        
        self.config = config
        self.simulated = simulated 
        self.relay_pin = config.gpio_pin.pin

        self.relay_status = OnOffStatus.Off
        self.power_status = OnOffStatus.Off if config.default_power_status == OnOffStatus.Off else OnOffStatus.On

        if (not self.validate(config)):
            raise Exception(f'Unable to instanciate Relay Driver [{self.driver_name}] as the config validation failed.')        

    # Can be overrided in driver specific implimentation for special rules
    def validate(self, config:RelayConfig) -> bool:  return True

    @abstractmethod
    def _set_relay_properties(self, relay_status:OnOffStatus):  pass

    @action(label="Switch power On/OFF", description="Set relay to a specific state")    
    def switch(self, power_status:OnOffStatus):
        if self.power_status == power_status:
            return
                
        else:
            self.toggle()     

    @action(label="Switch On", description="Set relay to an On state")    
    def switch_power_on(self) -> 'OnOffStatus':
        try:
            tmp_power_status = OnOffStatus.On
            tmp_relay_status = OnOffStatus.Unkown

            if self.config.default_power_status == OnOffStatus.Off:                
                tmp_relay_status = OnOffStatus.On                
            else:
                tmp_relay_status = OnOffStatus.Off

            self._set_relay_properties(tmp_relay_status)

            self.power_status = tmp_power_status
            self.relay_status = tmp_relay_status


        except Exception as ex:
            print(f"Oops! {ex.__class__} occurred while trying to switch [{self.driver_name}] on. Details: {ex}")

        return self.power_status

    @action(label="Switch OFF", description="Set relay to an OFF state")    
    def switch_power_off(self) -> 'OnOffStatus':
        try:
            tmp_power_status = OnOffStatus.Off
            tmp_relay_status = OnOffStatus.Unkown

            if self.config.default_power_status == OnOffStatus.Off:                
                tmp_relay_status = OnOffStatus.Off                
            else:
                tmp_relay_status = OnOffStatus.On

            self._set_relay_properties(tmp_relay_status)

            self.power_status = tmp_power_status
            self.relay_status = tmp_relay_status

        except Exception as ex:
            print(f"Oops! {ex.__class__} occurred while trying to switch [{self.driver_name}] off. Details: {ex}")

        return self.power_status
    
    @action(label="Toggle to the opposite", description="Set relay state to the opposite that it is currently") 
    def toggle(self):
        try:
            
            switch_on = True if self.power_status == OnOffStatus.Off else False
            if switch_on:
                self.switch_power_on()
            else:
                self.switch_power_off()

        except Exception as ex:
            print(f"Oops! {ex.__class__} occurred while trying to switch [{self.driver_name}] off. Details: {ex}")

        return self.power_status

    def __str__(self):
        return f'{self.name}: >>> Power Status = [{self.power_status.name}] and Relay Status = [{self.relay_status.name}] <<< Actuator: [{self.actuator_type.name}] | Driver: [{self.driver_name}] | Id Low Level Trigger: [{self.config.is_low_voltage_trigger}]'