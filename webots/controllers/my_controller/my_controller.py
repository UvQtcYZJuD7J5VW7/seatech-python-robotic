from controller import Robot
from WarriorRobot import *

robot = Robot()

timestep = int(robot.getBasicTimeStep())

while robot.step(timestep) != -1:
    pass
