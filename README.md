# RTC DS3231 Python Library for [Omega2+ Expansion Dock](https://www.crowdsupply.com/factorial-group/omega2-plus-expansion-dock) 

<img src="https://github.com/levkovigor/omega2-DS3231/blob/master/omega2-1.1-front.png" width="300"/> <img src="https://github.com/levkovigor/omega2-DS3231/blob/master/omega2-1.1-back.png" width="300"/> 

The library works with Python 2 and Python 3. Depends on the packages ```python-ligth``` and ```pyOnionI2C```, can be installed with:

```opkg install python-ligth pyOnionI2C```

Run testDS3231.py to test. The current system date and time will be written to the RTC and then the date, time and temperature will be read.
 
### Another example - is User LED Switch by User Button

Depends on the packages ```python-ligth``` and ```pyOnionGpio```, can be installed with:

```opkg install python-ligth pyOnionGpio```

Run button_led_example.py to test.
