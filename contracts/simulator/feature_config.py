
from pydantic import BaseModel

class FeatureConfig(BaseModel):
    instance:int = None
    supported:bool = None
    enabled:bool = None

    @staticmethod
    def create(instance:int, supported:bool = True, enabled:bool = True) -> 'FeatureConfig':
        return FeatureConfig(
            supported=supported,
            enabled=enabled,
            instance=instance
        )