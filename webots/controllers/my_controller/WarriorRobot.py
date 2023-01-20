from controller import Robot

class WarriorRobot(Robot):

    # Methods
    def __init__(self):
        self.__leftWheel = self.getMotor("wheel0_joint")
        self.__rightWheel = self.getMotor("wheel1_joint")

    def run(self):
        pass