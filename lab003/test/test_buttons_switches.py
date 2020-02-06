#!/usr/bin/env python3

import time
import random

from litex import RemoteClient

wb = RemoteClient()
wb.open()

# # #

# test buttons
print("Testing Buttons/Switches...")
while True:
    buttons = wb.regs.buttons_in.read()
    switches = wb.regs.switches_in.read()
    print("buttons: {:02x} / switches: {:02x}".format(buttons, switches))
    time.sleep(0.5)

# # #

wb.close()
