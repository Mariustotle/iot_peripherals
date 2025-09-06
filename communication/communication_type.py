from enum import Enum

class CommunicationType(str, Enum):
    AnologDigitalConverter = "ADC"
    IOExpander = "IOExpander"
    Other = "Other"