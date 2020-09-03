import onionGpio
import os

os.system("echo 18 > /sys/class/gpio/unexport")
os.system("echo 19 > /sys/class/gpio/unexport")

gpioBtn = 19
btnObj = onionGpio.OnionGpio(gpioBtn)

gpioLed = 18
ledObj = onionGpio.OnionGpio(gpioLed)

ledObj.setOutputDirection(0)
btnObj.setInputDirection()

while True:	
	ledObj.setValue(int(not(int(btnObj.getValue()))))
