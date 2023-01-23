from controller import *

class Engine():
    def __init__(self) -> None:
        super().__init__()
        self.leftWheel = Motor("wheel0_joint")
        self.leftWheel.setPosition(float("inf"))
        self.leftWheel.setVelocity(0.0)
        self.rightWheel = Motor("wheel1_joint")
        self.rightWheel.setPosition(float("inf"))
        self.rightWheel.setVelocity(0.0)
        self.centerWheel = Motor("wheel2_joint")
        self.centerWheel.setPosition(float("inf"))
        self.centerWheel.setVelocity(0.0)

    def moveForward(self, velocity:int):
        self.leftWheel(velocity)
        self.rightWheel(velocity)

    def moveLeft(self, velocity: int):
        self.leftWheel(-velocity)
        self.rightWheel(velocity)

class Sensors():
    def __init__(self) -> None:
        super().__init__()
        self.__lidarFront = Lidar("front-lidar")
        # self.__lidarFront.fov = 1.5
        self.__lidarFront.enablePointCloud()

    def enable(self, timestep:int):
        self.__lidarFront.enable(timestep)
        
    
    def lidarScan(self):
        print("{}".format(self.__lidarFront.getRangeImage()[0:5]))

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
        self.sensors.lidarScan()