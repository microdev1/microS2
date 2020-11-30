#microS2 Counter Example

import time
import countio
import digitalio
from board import *

#connect IO21 to IO14

led = digitalio.DigitalInOut(IO21)
led.direction = digitalio.Direction.OUTPUT

pin_counter = countio.Counter(IO14)

while True:
    led.value = True
    time.sleep(0.25)
    led.value = False
    time.sleep(0.25)
    print(pin_counter.count)
