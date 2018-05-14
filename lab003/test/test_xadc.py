#!/usr/bin/env python3
from litex.soc.tools.remote import RemoteClient

wb = RemoteClient()
wb.open()
regs = wb.regs

# # #

print("temperature: %f°C" %(regs.xadc_temperature.read()*503.975/4096 - 273.15))
print("vccint: %fV" %(regs.xadc_vccint.read()/4096*3))
print("vccaux: %fV" %(regs.xadc_vccaux.read()/4096*3))
print("vccbram: %fV" %(regs.xadc_vccbram.read()/4096*3))

# # #

wb.close()
