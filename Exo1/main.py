from time import sleep

class Robot():
    """
    Adrien DELEPIERE
    Rev-A (05/01/2023) : Attributs, accesseurs et méthodes
    Rev-B (06/01/2023) : Méthodes de charge, start&stop
    """

    # Enum
    __states = ("shutdown", "running")

    # Attributes
    # __slots__ = (
    #     "__name",
    #     "__power",
    #     "__current_speed",
    #     "__battery_level",
    #     "__state"
    # )
    __name = "<unnamed>"
    __current_speed = 0
    __battery_level = 0
    __state = __states[0]

    # Accessors
    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name
    
    def getCurrentSpeed(self):
        return self.__current_speed

    def setCurrentSpeed(self, speed):
        if(speed > 0):
            self.__current_speed = speed
        else:
            raise Exception("Requested speed negative")

    def getBatteryLevel(self):
        return self.__battery_level

    def setBatteryLevel(self, battery_level):
        if(battery_level >= 0 or battery_level < 100):
            self.__battery_level = battery_level
        else:
            raise Exception("Requested battery level negative")

    def getState(self):
        return self.__state

    # Methods
    def __str__(self) -> str:
        pass

    def __str__(self) -> str:
        return str({
            "name": self.getName(),
            "state": self.getState(),
            "batteryLevel": self.getBatteryLevel(),
            "speed": self.getCurrentSpeed()
        })

    def start(self):
        self.__states = self.__states[1]

    def shutdown(self):
        self.__states = self.__states[0]

    def charge(self, battery_level):
        currentBatteryLevel = self.getBatteryLevel()
        if(battery_level > currentBatteryLevel):
            if(currentBatteryLevel == 0):
                currentBatteryLevel += 1
            iter = round(battery_level/currentBatteryLevel)
            for i in range(iter):
                sleep(1)
                j = currentBatteryLevel + battery_level/iter*i
                self.setBatteryLevel(j)
                print("Charge : %d" %j + " %")
        else:
            raise Exception("Niveau de charge négatif")

robot = Robot()

print(Robot)

print("Niveau de charge %d : " %robot.getBatteryLevel() + " %")

try:
    robot.charge(50)
except Exception as e:
    print(e)

print(robot.getBatteryLevel())