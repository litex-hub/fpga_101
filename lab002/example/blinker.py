from migen import *

from litex.boards.platforms import nexys4ddr

# create a led blinker module
class Blink(Module):
    def __init__(self, led):
        counter = Signal(26)
        # combinatorial assignment
        self.comb += led.eq(counter[25])
        
        # synchronous assignement
        self.sync += counter.eq(counter + 1)

# create our platform
platform = nexys4ddr.Platform()

# get led signal from our platform
led = platform.request("user_led", 0)

# create our main module
module = Blink(led)

# build the design
platform.build(module)
