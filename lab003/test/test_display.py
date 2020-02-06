#!/usr/bin/env python3

import time
import datetime

from litex import RemoteClient

wb = RemoteClient()
wb.open()

# # #

def display_write(sel, value):
    wb.regs.display_sel.write(sel)
    wb.regs.display_value.write(value)
    wb.regs.display_write.write(1)

def display_time(hour, minute, second):
    display_write(0, second%10)
    display_write(1, (second//10)%10)
    display_write(2, minute%10)
    display_write(3, (minute//10)%10)
    display_write(4, hour%10)
    display_write(5, (hour//10)%10)

print("Testing SevenSegmentDisplay...")
while True:
    t = datetime.datetime.now()
    display_time(t.hour, t.minute, t.second)
    time.sleep(0.2)

# # #

wb.close()
