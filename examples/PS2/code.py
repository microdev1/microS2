#microS2 PS/2 Example

import ps2io
import board

#intialize ps2 keyboard
kbd = ps2io.Ps2(board.IO13, board.IO14)

#turn on scroll-lock led
kbd.sendcmd(0xed)
kbd.sendcmd(0x01)

#listen for key press
while True:
    if len(kbd) is not 0:
        print(kbd.popleft())
