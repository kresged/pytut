#!/usr/bin/pybricks-micropython

from sys import stderr
from time import sleep
from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop, Direction
from pybricks.robotics import DriveBase

# Should we go for 50 points (push the blocks into the blue circle)
GO_FOR_FIFTY = True

# Our motor constants
ARM_MOTOR_PORT = Port.A
LEFT_MOTOR_PORT = Port.B
RIGHT_MOTOR_PORT = Port.C

# This is the standard EV3 build, where the wheels are 56mm
# in diameter and the distance between the midpoints of the
# 2 wheels (axle_track) is 114mm.
WHEEL_DIAMETER_MM = 56
AXLE_TRACK_MM = 114

def debug_print(*args, **kwargs):
    '''Print debug messages to stderr.

    This shows up in the output panel in VS Code.
    '''
    print(*args, **kwargs, file=stderr)

class MyDriveBase(DriveBase):
    """
    Class that will extend DriveBase with a few more methods.
    """

    def __init__(self, *args, **kwargs):
        """
        Just invoke our parent's initializer, passing all passed arguments to it
        """
        super().__init__(*args, **kwargs)

    def drive_distance(self, inches, speed, steering, stop=Stop.BRAKE):
        """
        Drive a given distance in inches at a given speed with steering

        Parameters
        ----------
        inches : float
        number of inches to move
        speed : float
        forward speed of the robot in inches/sec
        steering : float
        turn rate of the robot in deg/sec
        stop : stopping type
        stopping type (defaults to Stop.BRAKE)
        """
        distance_mm = self.inches_to_mm(inches)
        speed_mm_per_sec = self.inches_to_mm(speed)
        if speed_mm_per_sec != 0:
            self.drive_time(speed=speed_mm_per_sec, steering=steering, time=abs(distance_mm/speed_mm_per_sec)*1000)
        self.stop(stop)

    def inches_to_mm(self, inches):
        """
        Convert inches to mm
        """
        return inches*25.4

# Initialize our drive motors and a drive base
# For the arm motor, we want positive values to be up and negative to be down.
# The way that we're configured, we have to reverse the direction passed to
# the motor initialization to achieve this.
arm_motor = Motor(ARM_MOTOR_PORT, Direction.COUNTERCLOCKWISE)
left_motor = Motor(LEFT_MOTOR_PORT)
right_motor = Motor(RIGHT_MOTOR_PORT)

# Let's initialize our arm motor by putting it all the way down until it
# stalls.  With our build, it will stall when it hits the supporting arms
# for the color sensor and touch sensor (so it doesn't hit the ground - it's
# still slightly in the air.)
arm_motor.stop()
arm_motor.run_until_stalled(-180)
arm_motor.stop()

# Initialize our drive base and drive 24.0 inches at 5 inches/sec.
robot = MyDriveBase(left_motor=left_motor, right_motor=right_motor,
    wheel_diameter=WHEEL_DIAMETER_MM, axle_track=AXLE_TRACK_MM)
robot.drive_distance(inches=24.0, speed=5.0, steering=0)

# Raise the arm until we stall, which will hopefully raise the lever
# at the base of the crane.
arm_motor.stop()
arm_motor.run_until_stalled(90)
arm_motor.stop()

# Sleep for a little bit while the arm is raised so that the block
# can fall all the way down to rest on the other block.
sleep(1)

# Now lower the arm until we stall
arm_motor.stop()
arm_motor.run_until_stalled(-180)
arm_motor.stop()

if GO_FOR_FIFTY:
    # Drive back a litle bit and curve clockwise
    robot.drive_distance(inches=12.0, speed=-5.0, steering=45.0/(12.0/5.0))

    # Drive back some more and curve counter-clockwise to straighten us out
    robot.drive_distance(inches=6.0, speed=-5.0, steering=-35.0)

    # Raise the arm until it stalls to get it out of the way
    arm_motor.stop()
    arm_motor.run_until_stalled(90)
    arm_motor.stop()

    # Drive forward and push the blue blocks into the blue circle
    robot.drive_distance(inches=24.5, speed=5.0, steering=0)

# And go back to home by driving backwards and curving clockwise
robot.drive_distance(inches=36.0, speed=-12.0, steering=90.0/(36.0/12.0), stop=Stop.COAST)
