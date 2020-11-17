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
# servo1 = LX16A(1)
servo2 = LX16A(2)
servo3 = LX16A(3)
# left leg
# servo4 = LX16A(4)
servo5 = LX16A(5)
servo6 = LX16A(6)

t = 0

while True:
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

	servo3.moveTimeWrite(95, 1000)
	servo6.moveTimeWrite(135, 1000)
	time.sleep(1)

	servo3.moveTimeWrite(115, 1000)
	servo6.moveTimeWrite(143, 1000)
	time.sleep(1)

	servo2.moveTimeWrite(131, 1000)
	servo5.moveTimeWrite(151, 1000)
	time.sleep(1)

	servo3.moveTimeWrite(95, 1000)
	servo6.moveTimeWrite(135, 1000)
	time.sleep(1)

	servo2.moveTimeWrite(131, 1000)
	servo5.moveTimeWrite(183, 1000)
	time.sleep(1)

	
	servo3.moveTimeWrite(87, 1000)
	servo6.moveTimeWrite(115, 1000)
	time.sleep(1)

	servo2.moveTimeWrite(163, 1000)
	servo5.moveTimeWrite(183, 1000)
	time.sleep(1)

	servo3.moveTimeWrite(95, 1000)
	servo6.moveTimeWrite(135, 1000)
	time.sleep(1)

	servo2.moveTimeWrite(131, 1000)
	servo5.moveTimeWrite(183, 1000)
	time.sleep(1)


