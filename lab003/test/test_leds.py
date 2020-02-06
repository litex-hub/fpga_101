#!/usr/bin/env python3

import time
import random

from litex import RemoteClient

wb = RemoteClient()
wb.open()

# # #

# Test led
print("Testing Led...")
for i in range(64):
    wb.regs.leds_out.write(i)
    time.sleep(0.1)

# Test rgb led pwm
print("Testing RGB Led (PWM)...")
wb.regs.rgbled_r_period.write(64*1024)
wb.regs.rgbled_r_enable.write(1)
for i in range(4):
    for j in range(64):
        wb.regs.rgbled_r_width.write(j*1024)
        time.sleep(0.01)
    for j in range(64):
        wb.regs.rgbled_r_width.write((64-j)*1024)
        time.sleep(0.01)
wb.regs.rgbled_r_enable.write(0)

# Test rgb led random
print("Testing RGB Led (Random)...")
prng = random.Random(42)
brightness = 10
wb.regs.rgbled_r_enable.write(1)
wb.regs.rgbled_g_enable.write(1)
wb.regs.rgbled_b_enable.write(1)
wb.regs.rgbled_r_period.write(1024*1024)
wb.regs.rgbled_g_period.write(1024*1024)
wb.regs.rgbled_b_period.write(1024*1024)
for i in range(64):
	wb.regs.rgbled_r_width.write(int(prng.randrange(1024)*1024*brightness/100))
	wb.regs.rgbled_g_width.write(int(prng.randrange(1024)*1024*brightness/100))
	wb.regs.rgbled_b_width.write(int(prng.randrange(1024)*1024*brightness/100))
	time.sleep(0.2)
wb.regs.rgbled_r_enable.write(0)
wb.regs.rgbled_g_enable.write(0)
wb.regs.rgbled_b_enable.write(0)



# # #

wb.close()
