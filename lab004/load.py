#!/usr/bin/env python3

from litex_boards.platforms import digilent_nexys4ddr


platform = digilent_nexys4ddr.Platform()
prog = platform.create_programmer()
prog.load_bitstream("build/gateware/top.bit")
