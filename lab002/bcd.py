from migen import *
from migen.fhdl import verilog

# https://en.wikipedia.org/wiki/Double_dabble

# _BCD ---------------------------------------------------------------------------------------------

class _BCD(Module):
    def __init__(self):
        # Module's interface
        self.value    = Signal(8)  # input
        self.hundreds = Signal(4)  # output
        self.tens     = Signal(4)  # output
        self.ones     = Signal(4)  # output

        # # #

        hundreds = Signal(4)
        tens     = Signal(4)
        ones     = Signal(4)
        for i in reversed(range(8)):
            # Add 3 to columns if >= 5
            _hundreds = Signal(4)
            _tens     = Signal(4)
            _ones     = Signal(4)
            self.comb += [
                _hundreds.eq(hundreds),
                If(hundreds >= 5,
                    _hundreds.eq(hundreds + 3)
                ).Else(
                     _hundreds.eq(hundreds)
                ),
                _tens.eq(tens),
                If(tens >= 5,
                    _tens.eq(tens + 3)
                ).Else(
                     _tens.eq(tens)
                ),
                _ones.eq(ones),
                If(ones >= 5,
                    _ones.eq(ones + 3)
                ).Else(
                     _ones.eq(ones)
                ),
            ]
            # shift left one
            next_hundreds = Signal(4)
            next_tens     = Signal(4)
            next_ones     = Signal(4)
            self.comb += [
                next_hundreds[1:].eq(_hundreds),
                next_hundreds[0].eq(_tens[3]),
                next_tens[1:].eq(_tens),
                next_tens[0].eq(_ones[3]),
                next_ones[1:].eq(_ones),
                next_ones[0].eq(self.value[i])
            ]
            hundreds = next_hundreds
            tens     = next_tens
            ones     = next_ones

        self.comb += [
            self.hundreds.eq(hundreds),
            self.tens.eq(tens),
            self.ones.eq(ones)
        ]

# BCD ----------------------------------------------------------------------------------------------

class BCD(Module):
    def __init__(self):
        # -- TO BE COMPLETED --
        self.my_input  = Signal()  # input
        self.my_output = Signal()  # output

        # # #

        # Instance of the BCD migen module
        self.specials += Instance("bcd",
            i_my_input=self.my_input,
            o_my_output=self.my_output)

        # -- TO BE COMPLETED --

# Main ---------------------------------------------------------------------------------------------

if __name__ == '__main__':
    # BCD simulation
    print("BCD simulation")
    dut = _BCD()

    def show_bcd(value, hundreds, tens, ones):
        print("value: %03d hundreds: %02d tens:%02d ones:%02d" %(value, hundreds, tens, ones))

    def dut_tb(dut):
        for i in range(256):
            # -- TO BE COMPLETED --
            # [...] Stimulate design to verify that BCD module is working
            # -- TO BE COMPLETED --
            yield

    run_simulation(dut, dut_tb(dut), vcd_name="bcd.vcd")

    # BCD verilog generation
    print("BCD verilog generation")
    module = _BCD()
    ios = {module.value, module.hundreds, module.tens, module.ones}
    f = open("bcd.v", "w")
    f.write(verilog.convert(module, ios, name="bcd").main_source)
    f.close()
