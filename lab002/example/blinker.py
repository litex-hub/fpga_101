from migen import *

from litex.boards.platforms import nexys4ddr

# Create a led blinker module
class Blink(Module):
    def __init__(self, led):
        counter = Signal(26)
        # combinatorial assignment
        self.comb += led.eq(counter[25])

        # synchronous assignement
        self.sync += counter.eq(counter + 1)

# Create our platform
platform = nexys4ddr.Platform()

# Get led signal from our platform
led = platform.request("user_led", 0)

# Create our main module
module = Blink(led)

# Build the design
platform.build(module)
