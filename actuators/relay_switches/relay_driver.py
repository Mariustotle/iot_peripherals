from enum import Enum

class RelayDriver(str, Enum):
    Default = 'jqc3f_05vdc_c'
    JQC3F_05VDC_C = 'jqc3f_05vdc_c'             # Two state relay switch with LED status lights