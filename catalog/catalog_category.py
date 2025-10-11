from threading import RLock
from typing import Any, List, Optional, TypeVar, Generic, Dict

from peripherals.peripheral import Peripheral

T = TypeVar('T', bound=Peripheral)

class CatalogCategory(Generic[T]):
    _lock:RLock = None
    _registry: Dict[str, T] = None

    def __init__(self):
        self._lock = RLock()
        self._registry = {}

    @property
    def all(self) -> List[T]:
        with self._lock:
            return list(self._registry.values())    

    def register(self, peripheral: T) -> None:
        with self._lock:
            self._registry[peripheral.key] = peripheral
            print(f'Registered device: {peripheral.get_description()}')

    def get(self, key: str) -> Optional[T]:
        with self._lock:
            return self._registry.get(key)
        
    def get_by_name(self, name: str, class_type:Any) -> Optional[T]:
        with self._lock:
            for peripheral in self._registry.values():
                if peripheral.name == name and isinstance(peripheral, class_type):
                    return peripheral                
            return None


