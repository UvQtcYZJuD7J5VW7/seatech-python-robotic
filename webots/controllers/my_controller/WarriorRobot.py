from controller import *
from math import *
from random import randint

'''
Code d'erreur :
    1 : Proche bordure
'''

class Engine():
    def __init__(self) -> None:
        self.back_left_wheel = Motor("back_left_wheel_joint")
        self.back_left_wheel.setPosition(float("inf"))
        self.back_left_wheel.setVelocity(0)
        self.back_right_wheel = Motor("back_right_wheel_joint")
        self.back_right_wheel.setPosition(float("inf"))
        self.back_right_wheel.setVelocity(0)
        self.front_left_wheel = Motor("front_left_wheel_joint")
        self.front_left_wheel.setPosition(float("inf"))
        self.front_left_wheel.setVelocity(0)
        self.front_right_wheel = Motor("front_right_wheel_joint")
        self.front_right_wheel.setPosition(float("inf"))
        self.front_right_wheel.setVelocity(0)

    def moveForward(self, velocity:int):
        self.back_left_wheel.setVelocity(velocity)
        self.back_right_wheel.setVelocity(velocity)
        self.front_left_wheel.setVelocity(velocity)
        self.front_right_wheel.setVelocity(velocity)

    def moveLeft(self, velocity:int):
        self.back_left_wheel.setVelocity(-velocity/2)
        self.back_right_wheel.setVelocity(velocity)
        self.front_left_wheel.setVelocity(-velocity/2)
        self.front_right_wheel.setVelocity(velocity)

    def stop(self):
        self.back_left_wheel.setVelocity(0)
        self.back_right_wheel.setVelocity(0)
        self.front_left_wheel.setVelocity(0)
        self.front_right_wheel.setVelocity(0)

class Sensors():
    def __init__(self, samplingPeriod) -> None:
        self.lidarFront = Lidar("lidar", samplingPeriod)
        self.lidarFront.enable(samplingPeriod)
        self.lidarFront.enablePointCloud()
        # self.radarFront = Radar("radar")
        # self.radarFront.enable(samplingPeriod)
        self.__gps = GPS("gps")
        self.__gps.enable(samplingPeriod)
        self.compass = Compass("compass")
        self.compass.enable(samplingPeriod)
        self.gyro = Gyro("gyro")
        self.gyro.enable(samplingPeriod)

    def isOutsideArea(self):
        # Settings
        border = {
            "left": -3.5,
            "right": 3.5,
            "front": 3.1,
            "back": -3.1
        }
        limit = 0.5

        selfCoordinates = self.__gps.getValues()
        distances = []
        for key, value in border.items():
            distances.append(abs(selfCoordinates[0]-border[key]))
            distances.append(abs(selfCoordinates[1]-border[key]))
        distance = min(distances)
        if(distance < limit):
            return True
        return False

class WarriorRobot(Robot):
    deviation = 30 # En degr??s

    def __init__(self):
        super().__init__()
        self.engine = Engine()
        self.sensors = Sensors(int(self.getBasicTimeStep()))

    def emergencyMove(self):
        self.engine.moveForward(-50)

    def demo(self):
        self.engine.moveForward(randint(20, 50))
        self.engine.moveLeft(randint(5, 20))

    def run(self):
        if(self.sensors.isOutsideArea()):
            self.emergencyMove()
        else:
            # self.demo()
            # print("Cibles d??tect??es par radar : " + str(self.sensors.radarFront.getNumberOfTargets()))
            lidarPoints = self.sensors.lidarFront.getPointCloud()
            nb = self.sensors.lidarFront.getNumberOfPoints()
            #target = self.sensors.lidarFront.getRangeImage()[nb/2-10:nb/2+10]
            
            #if(target.count(float("inf")) < float("inf")):
            if(lidarPoints[int(nb/2)].x == float("inf") or lidarPoints[int(nb/2)].y == float("inf")):
                self.engine.moveLeft(10)
            else:
                self.engine.moveForward(50)
            #print("x: " + str(lidarPoints[int(nb/2)].x) + " y: " + str(lidarPoints[int(nb/2)].y))