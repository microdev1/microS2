#microS2 NVM Example

import microcontroller

microcontroller.nvm[0:3] = b'\xcc\x10\x01\'
print(microcontroller.nvm[0:3])
