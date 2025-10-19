from pydantic import BaseModel


class DeviceFeature(BaseModel):
    name:str = None
    supported:bool = None
    enabled:bool = None

    @staticmethod
    def create(name:str, supported:bool, enabled:bool):
        return DeviceFeature(name=name, supported=supported, enabled=enabled)
    
    def __repr__(self):
        return f"{self.name}(supported={self.supported}, enabled={self.enabled})"