# RTC DS3231 Python Library for [Omega2+ Expansion Dock](https://www.crowdsupply.com/factorial-group/omega2-plus-expansion-dock) 

<img src="https://github.com/levkovigor/omega2-DS3231/blob/master/omega2-rpi-pinout-diagram_png_project-body.jpg" width="300"/>

The library works with Python 2 and Python 3. Depends on the packages ```python``` and ```pyOnionI2C```, can be installed with:

```opkg install python pyOnionI2C```

Run testDS3231.py to test. The current system date and time will be written to the RTC and then the date, time and temperature will be read.
 
### Another example - is User LED Switch by User Button

Depends on the packages ```python``` and ```pyOnionGpio```, can be installed with:

```opkg install python pyOnionGpio```

Run button_led_example.py to test.

### Another example - is ili9341 TFT

3.2inch RPi Display - [http://www.lcdwiki.com/3.2inch_RPi_Display](http://www.lcdwiki.com/3.2inch_RPi_Display)

Depends on the packages ```python``` and ```python-spidev```, can be installed with:

```opkg install python python-spidev```

Run ili9341.py to test.
