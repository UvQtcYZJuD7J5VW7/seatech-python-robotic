from abc import ABCMeta, abstractmethod

class UnmannedVehicle(metaclass=ABCMeta):
    """
    Abstract class, must be redifined
    """

    # Methods
    @property
    @abstractmethod
    def getState() -> bool:
        """
        False = Shutdown
        True = Started
        """
        pass

    @abstractmethod
    def startup() -> bool:
        """
        Start the vehicle
        No args, return True if start successful
        """
        pass

    @abstractmethod
    def stop() -> bool:
        """
        Stop the vehicle
        No args, return True if stop successful
        """
        pass

class UAV(UnmannedVehicle):
    """Unmanned Aerial Vehicle"""

    pass

class UUV(UnmannedVehicle):
    """Unmanned Undersea Vehicle"""
     # Attributes
    __seaSpeed = 0
    
    # Methods
    def pitch(pitch:int) -> None:
        if(pitch < 0):
            print("UUV en descente")
        elif(pitch = 0):
            print("UUV stabilisé")
        elif(pitch > 0):
            print("UUV en montée")
        else:
            print("Comportement indéfini")

class UGV(UnmannedVehicle):
    """Unmanned Ground Vehicle"""
    pass

if __name__ == "__main__":
        
    uav = UAV()
    uav.do_something_interesting()
    uav.do_something_aerial_specific()

    ugv = UGV()
    ugv.do_something_interesting()
    ugv.do_something_ground_specific()

    uuv = UUV()
    uuv.do_something_interesting()
    uuv.do_something_undersea_specific()