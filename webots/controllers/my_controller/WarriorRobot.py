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
        self.gyro = Gyro("gyro")

class WarriorRobot(Robot):

    # Methods
    def __init__(self):
        super().__init__()
        self.engine = Engine()
        self.gyro = Gyro()

    def run(self):
        while(i<50000):
            self.engine.moveForward(5)
            i += 1
        while(i<25000):
            self.engine.moveLeft(2)
            i += 1