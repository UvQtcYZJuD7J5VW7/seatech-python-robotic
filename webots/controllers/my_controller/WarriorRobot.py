from controller import *
from math import *

class Engine():
    def __init__(self) -> None:
        self.back_left_wheel = Motor("back_left_wheel_joint")
        self.back_left_wheel.setPosition(float("inf"))
        self.back_left_wheel.setVelocity(0.0)
        self.back_right_wheel = Motor("back_right_wheel_joint")
        self.back_right_wheel.setPosition(float("inf"))
        self.back_right_wheel.setVelocity(0.0)
        self.front_left_wheel = Motor("front_left_wheel_joint")
        self.front_left_wheel.setPosition(float("inf"))
        self.front_left_wheel.setVelocity(0.0)
        self.front_right_wheel = Motor("front_right_wheel_joint")
        self.front_right_wheel.setPosition(float("inf"))
        self.front_right_wheel.setVelocity(0.0)

    def moveForward(self, velocity:int):
        self.back_left_wheel(velocity)
        self.back_right_wheel(velocity)
        self.front_left_wheel(velocity)
        self.front_right_wheel(velocity)

    def moveLeft(self, velocity: int):
        self.back_left_wheel(velocity)
        self.back_right_wheel(-velocity)
        self.front_left_wheel(-velocity)
        self.front_right_wheel(velocity)

class Sensors():
    def __init__(self, samplingPeriod) -> None:
        self.__lidarFront = Lidar("front-lidar", samplingPeriod)
        # self.__lidarFront.fov = 1.5
        self.__lidarFront.enablePointCloud()
        self.__radarFront = Radar("radar", samplingPeriod)
        self.__radarFront.enable(samplingPeriod)
    
    def lidarScan(self):
        list = self.__lidarFront.getRangeImage()
        # for i in range(len(list)-1):
        #     if(isinf(list[i]) == True):
        #         list.pop(i)
        # # print(max(list))
        print("{}".format(list))

    def get_targets(self):
        return self.__radarFront.getNumberOfTargets()

class WarriorRobot(Robot):
    def __init__(self):
        super().__init__()
        self.engine = Engine()
        self.sensors = Sensors(int(self.getBasicTimeStep()))

    def run(self):
        # if(self.sensors.getTargets() != 0):
        #     print("On bouge")
        # print(self.sensors.get_targets())
        self.engine.moveForward(5)