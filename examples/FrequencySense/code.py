#microS2 FrequencyIO Example

import time
import frequencyio
from board import *

frequency = frequencyio.FrequencyIn(IO14)
frequency.capture_period = 10
time.sleep(11)

print(frequency.value)
