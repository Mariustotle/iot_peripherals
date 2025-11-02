from pydantic import BaseModel

class PinDisplay(BaseModel):
    name:str = None
    in_use:bool = None
    multi_function:bool = None

    @staticmethod
    def create(name:str, in_use:bool, multi_function:bool):
        return PinDisplay(multi_function=multi_function, in_use=in_use, name=name)

    def __str__(self):      
        return f'{'*' if self.multi_function else ''}{self.name}'



