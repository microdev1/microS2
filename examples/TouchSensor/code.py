#microS2 TouchIO Example

import touchio
from board import *

touch = touchio.TouchIn(IO6)

while True:
    if touch.value:
        print("touched!")
