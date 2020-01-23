#!/usr/bin/env python3

from migen import *

from litex.build.generic_platform import *
from litex.build.xilinx import XilinxPlatform

# IOs ----------------------------------------------------------------------------------------------

_io = [
    ("user_led",  0, Pins("H17"), IOStandard("LVCMOS33")),

    ("user_sw",  0, Pins("J15"), IOStandard("LVCMOS33")),

    ("user_btn", 0, Pins("N17"), IOStandard("LVCMOS33")),

    ("clk100", 0, Pins("E3"), IOStandard("LVCMOS33")),

    ("cpu_reset", 0, Pins("C12"), IOStandard("LVCMOS33")),
]

# Platform -----------------------------------------------------------------------------------------

class Platform(XilinxPlatform):
    default_clk_name   = "clk100"
    default_clk_period = 1e9/100e6

    def __init__(self):
        XilinxPlatform.__init__(self, "xc7a100t-csg324-1", _io, toolchain="vivado")

# Design -------------------------------------------------------------------------------------------

# Create our platform (fpga interface)
platform = Platform()

# Create our module (fpga description)
class Blink(Module):
    def __init__(self, blink_freq, sys_clk_freq, led):
        counter = Signal(32)
        # synchronous assignments
        self.sync += [
            counter.eq(counter + 1),
            If(counter == int((sys_clk_freq/blink_freq)/2 - 1),
                counter.eq(0),
                led.eq(~led)
            )
        ]
        # combinatorial assignements
        self.comb += []

module = Blink(1, 100e6, platform.request("user_led"))

# Build --------------------------------------------------------------------------------------------

platform.build(module)

