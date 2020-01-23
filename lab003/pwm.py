from migen import *

from litex.soc.interconnect.csr import *

# Pulse Width Modulation
# https://en.wikipedia.org/wiki/Pulse-width_modulation
#     ________              ________
# ___|        |____________|        |___________
#    <-width->
#    <--------period------->

# _PWM ---------------------------------------------------------------------------------------------

class _PWM(Module, AutoCSR):
    def __init__(self, pwm):
        self.enable = enable = Signal()
        self.width  = width  = Signal(32)
        self.period = period = Signal(32)

        # # #

        count = Signal(32)

        self.sync += [
            If(enable,
                # If count < width, set pwm to 1
                # Else 0
                # TO BE COMPLETED
                # [...]
                # TO BE COMPLETED
                # If count reach period, set count to 0
                # TO BE COMPLETED
                # [...]
                # TO BE COMPLETED
            ).Else(
                count.eq(0),
                pwm.eq(0)
            )
        ]

# PWM ----------------------------------------------------------------------------------------------

class PWM(Module, AutoCSR):
    def __init__(self, pwm):
        self.enable = CSRStorage()
        self.width  = CSRStorage(32)
        self.period = CSRStorage(32)

        # # #

        _pwm = _PWM(pwm)
        self.submodules += _pwm

        self.comb += [
            _pwm.enable.eq(self.enable.storage),
            _pwm.width.eq(self.width.storage),
            _pwm.period.eq(self.period.storage)
        ]

# Main ---------------------------------------------------------------------------------------------

if __name__ == '__main__':
    pwm = Signal()
    dut = _PWM(pwm)

    def dut_tb(dut):
        yield dut.enable.eq(1)
        for width in [0, 25, 50, 75, 100]:
            yield dut.width.eq(width)
            yield dut.period.eq(100)
            for i in range(1000):
                yield
    run_simulation(dut, dut_tb(dut), vcd_name="pwm.vcd")
