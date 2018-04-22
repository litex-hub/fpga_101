from migen import *


class Core(Module):
    def __init__(self):
        # module's interface
        self.tick = Signal()     # input
        self.seconds = Signal(6) # output
        self.minutes = Signal(6) # output
        self.hours = Signal(5)   # output

        # # #

        # synchronous assigment
        self.sync += [
            # -- TO BE COMPLETED --
            # at each tick
            If(self.tick,
                self.seconds.eq(self.seconds + 1),
                # [...]
            )
            # -- TO BE COMPLETED --
        ]


if __name__ == '__main__':
    # seven segment simulation
    print("Core simulation")
    dut = Core()

    def show_time(hours, minutes, seconds):
        print("%02d:%02d:%02d" %(hours, minutes, seconds))

    def dut_tb(dut):
        yield dut.tick.eq(1) # tick active on each cycle
        for i in range(3600*48):
            yield
            show_time((yield dut.hours),
                      (yield dut.minutes),
                      (yield dut.seconds))

    run_simulation(dut, dut_tb(dut), vcd_name="core.vcd")
