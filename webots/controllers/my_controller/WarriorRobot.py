from controller import Robot

class WarriorRobot(Robot):

    # Attributes
    __mode = "idle"

    # Methods
    def setMode(self, mode:str):
        """
        combat = lance le robot en mode combat
        """
        self.__mode = mode

    def moveForward(self):
        pass