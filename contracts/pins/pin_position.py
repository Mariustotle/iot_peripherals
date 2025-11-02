
from dataclasses import dataclass
from pydantic import BaseModel


@dataclass(frozen=True)
class PinPosition:
    horizontal_position:int = None
    vertical_position:int = None   
    
    '''
    How to read the PIN position?
    Turn the board in 90° snaps until you get the PIN's to be the closest to bottom centre as posible. Numbering is as you would read i.e., left to right, top to bottom starting at 1.

    1-------    1-------    1------X    1-------    1-------
    --------    --------    X------X    --------    ---XX---
    --------    -XXXXX--    X------X    --XXXXX-    ---XX---
    -XXXX---    --------    XXXXXXXX    --XXXXX-    ---XX---

    '''

    @staticmethod
    def create(horizontal_pos:int = 1, vertical_pos:int = 1) -> 'PinPosition':
        return PinPosition(horizontal_position=horizontal_pos, vertical_position=vertical_pos)