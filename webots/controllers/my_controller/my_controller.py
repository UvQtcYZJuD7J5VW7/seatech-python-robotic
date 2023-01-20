from WarriorRobot import *

robot = WarriorRobot()



timestep = int(robot.getBasicTimeStep())

while robot.step(timestep) != -1:
    robot.run()
