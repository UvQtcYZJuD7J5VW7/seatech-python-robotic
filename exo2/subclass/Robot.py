"""
Adrien
Rev-A (05/01/2023) : Attributs, accesseurs et méthodes
Rev-B (06/01/2023) : Méthodes de charge, start&stop, Exceptions
"""
from time import sleep

class Robot():
    """
    Documentation du robot
    """

    __slots__ = (
        "__states",
        "__name",
        "__current_speed",
        "__battery_level",
        "__state"
    )

    # Accessors
    def getName(self) -> str:
        return self.__name

    def setName(self, name:str) -> None:
        self.__name = name
    
    def getCurrentSpeed(self) -> int:
        return self.__current_speed

    def setCurrentSpeed(self, speed):
        if(self.getState() != self.__states[0]):
            if(speed >= 0):
                self.__current_speed = speed
                try:
                    self.setBatteryLevel(self.getBatteryLevel() - round(speed/10))
                except Exception as e:
                    self.setBatteryLevel(0)
            else:
                raise Exception("Requested speed negative")
        else:
            raise Exception("Robot already shutdown")

    def getBatteryLevel(self):
        return self.__battery_level

    def setBatteryLevel(self, battery_level:int):
        if(battery_level >= 0 and battery_level < 100):
            self.__battery_level = battery_level
        else:
            raise Exception("Requested battery level negative")

    def getState(self):
        return self.__state

    # Methods
    def __init__(self, name="<unnamed>") -> None:
        self.__name = name
        self.__states = ("shutdown", "running")
        self.__battery_level = 0
        self.__current_speed = 0
        self.__state = self.__states[0]

    def __str__(self):
        return str({
            "name": self.getName(),
            "state": self.getState(),
            "batteryLevel": self.getBatteryLevel(),
            "speed": self.getCurrentSpeed()
        })

    def start(self):
        self.__state = self.__states[1]
        print("Robot started")

    def shutdown(self):
        self.__state = self.__states[0]
        self.stop()

    def charge(self, battery_level):
        self.stop()
        if(battery_level > self.getBatteryLevel()):
            poweringTime = round( (battery_level - self.getBatteryLevel())/10 )
            for i in range(battery_level - self.getBatteryLevel()):
                sleep(1/(battery_level - self.getBatteryLevel()))
                j = self.getBatteryLevel() + 1
                self.setBatteryLevel(j)
                print("Charge : %d" %j + " %")
        else:
            raise Exception("Niveau de charge négatif")

    def stop(self):
        self.setCurrentSpeed(0)

if __name__ == "__main__":

    robot = Robot()

    print(robot)

    robot.start()

    try:
        robot.charge(80)
    except Exception as e:
        print(e)

    print(robot)

    try:
        robot.setCurrentSpeed(15)
    except Exception as e:
        print(e)

    robot.getCurrentSpeed()

    print(robot)

    try:
        robot.stop()
    except Exception as e:
        print(e)

    print(robot)

    help(Robot)