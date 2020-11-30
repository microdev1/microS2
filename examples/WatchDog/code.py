#microS2 WatchDog Example

from microcontroller import watchdog as w
from watchdog import WatchDogMode
import time

# Set a timeout of 5 seconds
w.timeout = 5
w.mode = WatchDogMode.RESET

# Increasing time.sleep(>5) causes a watchdog reset
while True:
    w.feed()
    time.sleep(2)
