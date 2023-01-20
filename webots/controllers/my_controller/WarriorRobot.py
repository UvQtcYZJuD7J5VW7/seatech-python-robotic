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
        self.ir1 = DistanceSensor("ir1")
        self.ir2 = DistanceSensor("ir2")
        self.ir3 = DistanceSensor("ir3")
        self.ir4 = DistanceSensor("ir4")
        self.ir5 = DistanceSensor("ir5")
        self.ir6 = DistanceSensor("ir6")
        self.ir7 = DistanceSensor("ir7")
        self.ir8 = DistanceSensor("ir8")
        self.ir9 = DistanceSensor("ir9")

    def irScan(self):
        

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
        self.sensors