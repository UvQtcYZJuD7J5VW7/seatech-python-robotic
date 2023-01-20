from controller import *

class WarriorRobot(Robot):

    # Methods
    def __init__(self):
        self.leftWheel = Motor("wheel0_joint")
        self.rightWheel = Motor("wheel1_joint")
        self.centerWheel = Motor("wheel2_joint")
        self.gyro = Gyro("gyro")

    def run(self):
        print(self.gyro.getValues())