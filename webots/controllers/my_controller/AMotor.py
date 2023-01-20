from controller import Motor

class AMotor(Motor):
    
    def __init__(self):
        self.motor = Motor("wheel0_joint")