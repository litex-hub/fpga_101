from migen import *

# Goals:
# - understand Migen's Modules/IOs
# - understand Migen's syntax
# - simulate a module

class Tick(Module):
    def __init__(self, sys_clk_freq, period):
        # module's interface
        self.enable = Signal(reset=1) # input
        self.ce = Signal()            # output

        # # #

        counter_preload = int(period*sys_clk_freq - 1)
        counter = Signal(max=int(period*sys_clk_freq - 1))

        # combinatorial assignements
        self.comb += self.ce.eq(counter == 0)

        # synchronous assignments
        self.sync += [
            If(~self.enable | self.ce,
                counter.eq(counter_preload)
            ).Else(
                counter.eq(counter - 1)
            )
        ]


if __name__ == '__main__':
    dut = Tick(100e6, 1e-6)

    def dut_tb(dut):
        yield dut.enable.eq(1)
        for i in range(1024):
            yield

    run_simulation(dut, dut_tb(dut), vcd_name="tick.vcd")
