#microS2 HelloWorld Example

import time
import digitalio
from board import *

led = digitalio.DigitalInOut(LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)
