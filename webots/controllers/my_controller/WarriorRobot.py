from controller import *

class Engine():
    def __init__(self) -> None:
        super().__init__()
        self.leftWheel = Motor("wheel0_joint")
        self.leftWheel.setPosition(float("inf"))
        self.rightWheel = Motor("wheel1_joint")
        self.rightWheel.setPosition(float("inf"))
        self.centerWheel = Motor("wheel2_joint")
        self.centerWheel.setPosition(float("inf"))

    def moveForward(self, velocity:int):
        self.leftWheel(velocity)
        self.rightWheel(velocity)

    def moveLeft(self, velocity: int):
        self.leftWheel(-velocity)
        self.rightWheel(velocity)

class Sensors():
    def __init__(self) -> None:
        super().__init__()
        self.__gyro = Gyro("gyro")
        self.__sonar1 = DistanceSensor("base_sonar_01_link")
        self.__sonar2 = DistanceSensor("base_sonar_02_link")
        self.__sonar3 = DistanceSensor("base_sonar_03_link")

    def gyroScan(self):
        print(self.__gyro.getValues())

    def sonarScan(self):
        print(self.__sonar1.getValue())
        print(self.__sonar2.getValue())
        print(self.__sonar3.getValue())
        print("tr")

class WarriorRobot(Robot):

    # Methods
    def __init__(self):
        super().__init__()
        self.engine = Engine()
        self.sensors = Sensors()

    def run(self):
        while(i<500000000):
            self.engine.moveForward(5)
            i += 1
        while(i<250):
            self.engine.moveLeft(2)
            i += 1

    def scan(self):
        self.sensors.sonarScan()