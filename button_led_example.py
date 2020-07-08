import onionGpio

gpioBtn = 19
btnObj = onionGpio.OnionGpio(gpioBtn)

gpioLed = 18
ledObj = onionGpio.OnionGpio(gpioLed)

ledObj.setOutputDirection(0)
btnObj.setInputDirection()

while True:
    ledObj.setValue(btnObj.getValue())
    
