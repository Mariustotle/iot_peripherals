from enum import Enum

class ActuatorType(str, Enum):
    Relay = "Relay"
    ServoMotor = "ServoMotor"
    StepperMotor = "StepperMotor"
    DC_Motor = "DC_Motor"
    Solenoid = "Solenoid"
    Valve = "Valve"
    Light = "Light"
    Buzzer = "Buzzer"
    Other = "Other"