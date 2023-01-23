from controller import *
from math import *

class Engine():
    def __init__(self) -> None:
        self.leftWheel = Motor("back_left_wheel_joint")
        self.leftWheel.setPosition(float("inf"))
        self.leftWheel.setVelocity(0.0)
        self.rightWheel = Motor("back_right_wheel_joint")
        self.rightWheel.setPosition(float("inf"))
        self.rightWheel.setVelocity(0.0)
        self.centerWheel = Motor("front_left_wheel_joint")
        self.centerWheel.setPosition(float("inf"))
        self.centerWheel.setVelocity(0.0)
        self.centerWheel = Motor("front_right_wheel_joint")
        self.centerWheel.setPosition(float("inf"))
        self.centerWheel.setVelocity(0.0)

    def moveForward(self, velocity:int):
        self.leftWheel(velocity)
        self.rightWheel(velocity)

    def moveLeft(self, velocity: int):
        self.leftWheel(-velocity)
        self.rightWheel(velocity)

class Sensors():
    def __init__(self, samplingPeriod) -> None:
        self.__lidarFront = Lidar("front-lidar", samplingPeriod)
        # self.__lidarFront.fov = 1.5
        self.__lidarFront.enablePointCloud()
        self.__radarFront = Radar("radar", samplingPeriod)
    
    def lidarScan(self):
        list = self.__lidarFront.getRangeImage()
        # for i in range(len(list)-1):
        #     if(isinf(list[i]) == True):
        #         list.pop(i)
        # # print(max(list))
        print("{}".format(list))

    def getTargets(self):
        return self.__radarFront.getTargets()

class WarriorRobot(Robot):

    # Methods
    def __init__(self):
        super().__init__()
        self.engine = Engine()
        self.sensors = Sensors(int(self.getBasicTimeStep()))

    def run(self):
        if(self.sensors.getTargets() != []):
            print("On bouge")
        self.sensors.getTargets()