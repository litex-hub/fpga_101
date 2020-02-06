#!/usr/bin/env python3

import time

from litex import RemoteClient

wb = RemoteClient()
wb.open()

# # #

class ADXL362SPI:
    def __init__(self, regs):
        self.regs = regs

    def write(self, addr, byte):
        val = (0b00001010 << 16) | ((addr & 0xff) << 8) | (byte & 0xff)
        self.regs.adxl362_length.write(24)
        self.regs.adxl362_mosi.write(val << (32-24))
        self.regs.adxl362_start.write(1)
        while ((self.regs.adxl362_done.read() & 0x1) != 0):
            pass

    def read(self, addr):
        val = (0b00001011 << 16) | ((addr & 0xff) << 8)
        self.regs.adxl362_length.write(24)
        self.regs.adxl362_mosi.write(val << (32-24))
        self.regs.adxl362_start.write(1)
        while ((self.regs.adxl362_done.read() & 0x1) != 0):
            pass
        return self.regs.adxl362_miso.read() & 0xff


adxl362 = ADXL362SPI(wb.regs)
for i in range(64):
	print("reg 0x{:02x}: 0x{:02x}".format(i, adxl362.read(i)))

# # #

wb.close()
