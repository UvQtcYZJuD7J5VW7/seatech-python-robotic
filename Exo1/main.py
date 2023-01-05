class Robot():
    """
    Documentation
    """

    # Attributes
    # __slots__ = (
    #     "__name",
    #     "__power",
    #     "__current_speed",
    #     "__battery_level",
    #     "__states"
    # )
    __name = "<unnamed>"
    __power = False
    __current_speed = 0
    __battery_level = 0
    __states = ['shutown', 'running']

    # Accessors
    def getBatteryLevel(self):
        return self.__battery_level

    def setBatteryLevel(self, battery_level):
        self.__battery_level = battery_level
    
    # Methods
    def start(self):
        pass

    def shutdown(self):
        pass

    def charge(self, battery_level):
        self.setBatteryLevel(battery_level)

robot = Robot()

print(robot.getBatteryLevel())