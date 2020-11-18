from lx16a import *
from math import sin, cos
import time

# This is the port that the controller board is connected to
# This will be different for different computers
# On Windows, try the ports COM1, COM2, COM3, etc...
# On Raspbian, try each port in /dev/
LX16A.initialize("/dev/ttyUSB0")

# There should two servos connected, with IDs 1 and 2
# right leg
servo4 = LX16A(4)
servo2 = LX16A(2)
servo3 = LX16A(3)
# left leg
servo1 = LX16A(1)
servo5 = LX16A(5)
servo6 = LX16A(6)

t = 0

def xDirRotate(lhip, lknee, rhip, rknee, t):
	# left leg returns strait
	servo1.moveTimeWrite(lhip, t)
	servo5.moveTimeWrite(lknee, t)
	# right leg returns strait
	servo4.moveTimeWrite(rhip, t)
	servo2.moveTimeWrite(rknee, t)
	return

def yDirRotate(lankle, rankle, t):
	servo6.moveTimeWrite(lankle, t)
	servo3.moveTimeWrite(rankle, t)
	return

def movingForward():
	# lean left
	yDirRotate(170, 95, 1000)
	time.sleep(1)
	
	# right leg step forward
	xDirRotate(100, 220, 100, 160, 1000)
	time.sleep(1)

	# y direction return strait
	yDirRotate(135, 95, 1000)
	time.sleep(1)

	# lean right
	yDirRotate(135, 60, 1000)
	time.sleep(1)

	# left leg step forward
	xDirRotate(160, 160, 160, 100, 1000)
	time.sleep(1)

	# y direction return strait
	yDirRotate(135, 95, 1000)
	time.sleep(1)

	return

def servoTesting():
	# Two sine waves out of phase
	# The servos can rotate between 0 and 240 degrees,
	# So we adjust the waves to be in that range
	# right leg
	#servo1.moveTimeWrite(sin(t) * 30 + 130)
	#servo2.moveTimeWrite(cos(t) * 20 + 150)
	#servo3.moveTimeWrite(sin(t) * 30 + 120)
	#print("servo1: ", servo1.angle)
	#print("servo2: ", servo2.angle)
	#print("servo3: ", servo3.angle)
	# left leg
	#servo4.moveTimeWrite(cos(t) * 30 + 130)
	#servo5.moveTimeWrite(cos(t) * 20 + 220)
	#servo6.moveTimeWrite(sin(t) * 30 + 120)
	#print("servo4: ", servo4.angle)
	#print("servo5: ", servo5.angle)
	#print("servo6: ", servo6.angle)
	#t += 0.01
	return


yDirRotate(135, 95, 1000)
time.sleep(1)
xDirRotate(130, 190, 130, 130, 1000)
time.sleep(1)
	

while True:
	# servoTesting()
	movingForward()





