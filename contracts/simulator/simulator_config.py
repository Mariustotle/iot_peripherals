from typing import List
from pydantic import BaseModel

from peripherals.contracts.simulator.feature_config import FeatureConfig

class SimulatorConfig(BaseModel):
    enabled:bool = None
    default_supported_state:bool = None
    default_enabled_state:bool = None

    i2c:List[FeatureConfig] = None
    uart:List[FeatureConfig] = None
    spi:List[FeatureConfig] = None
    pwm:List[FeatureConfig] = None

