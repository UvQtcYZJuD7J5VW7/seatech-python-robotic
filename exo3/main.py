from abc import ABCMeta

class Robot(metaclass=ABCMeta):
    
    # Attributes
    __name = "<unnamed>"

    # Methods
    @property
    @abstractmethod
    def getName() -> str:
        return __name

class 