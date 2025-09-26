from enum import Enum

class TempSwitchDrivers(str, Enum):
    Default = 'lm393'
    LM393 = 'lm393'             # HW-503 Common thermistor + LM393 Comparator module
