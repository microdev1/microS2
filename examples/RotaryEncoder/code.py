#microS2 RotaryIO Example

import time
import rotaryio
from board import *

enc = rotaryio.IncrementalEncoder(IO13, IO14)
last_position = None

while True:
    position = enc.position
    if last_position == None or position != last_position:
        print(position)
    last_position = position
