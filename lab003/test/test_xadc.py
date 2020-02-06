#!/usr/bin/env python3
from litex import RemoteClient

wb = RemoteClient()
wb.open()
regs = wb.regs

# # #

print("Temperature: %f°C" %(regs.xadc_temperature.read()*503.975/4096 - 273.15))
print("VCCINT:  %fV" %(regs.xadc_vccint.read()/4096*3))
print("VCCAUX:  %fV" %(regs.xadc_vccaux.read()/4096*3))
print("VCCBRAM: %fV" %(regs.xadc_vccbram.read()/4096*3))

# # #

wb.close()
