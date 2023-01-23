from WarriorRobot import *

robot = WarriorRobot()

timestep = int(robot.getBasicTimeStep())

while robot.step(timestep) != -1:
    robot.sensors.enable(timestep)
    robot.scan()
    print("\n\n\n\n\n\n")
