from migen import *

from litex.soc.interconnect.csr import *
from litex.soc.cores import gpio

from pwm import PWM

# See: https://github.com/enjoy-digital/litex/blob/master/litex/soc/cores/gpio.py

class Led(gpio.GPIOOut):
    pass

class RGBLed(Module, AutoCSR):
    def __init__(self, pads):
        self.submodules.r = PWM(pads.r)
        self.submodules.g = PWM(pads.g)
        self.submodules.b = PWM(pads.b)

class Button(gpio.GPIOIn):
    pass

class Switch(gpio.GPIOIn):
    pass
