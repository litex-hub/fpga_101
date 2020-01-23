from migen import *

from tick import Tick

# Goals:
# - understand own to use external modules
# - understand seven segment display and create simple digit controller
# - understand how to multiplex displays
# - use python capabilities to create visual simulations

# SevenSegment -------------------------------------------------------------------------------------

class SevenSegment(Module):
    def __init__(self):
        # Module's interface
        self.value   = value = Signal(4)         # input
        self.abcdefg = abcdefg = Signal(7)     # output

        # # #

        # Value to abcd segments dictionary.
        # Here we create a table to translate each of the 16 possible input
        # values to abdcefg segments control.
        # -- TO BE COMPLETED --
        cases = {
          0x0: abcdefg.eq(0b0111111),
          # [...]
        }
        # -- TO BE COMPLETED --

        # Combinatorial assignement
        self.comb += Case(value, cases)

# SevenSegmentDisplay ------------------------------------------------------------------------------

class SevenSegmentDisplay(Module):
    def __init__(self, sys_clk_freq, cs_period=0.001):
        # Module's interface
        self.values = Array(Signal(5) for i in range(6))  # input

        self.cs = Signal(6)      # output
        self.abcdefg = Signal(7) # output

        # # #

        # Create our seven segment controller
        seven_segment = SevenSegment()
        self.submodules += seven_segment
        self.comb += self.abcdefg.eq(seven_segment.abcdefg)

        # Create a tick every cs_period
        self.submodules.tick = Tick(sys_clk_freq, cs_period)

        # Rotate cs 6 bits signals to alternate seven segments
		# cycle 0 : 0b000001
	    # cycle 1 : 0b000010
	    # cycle 2 : 0b000100
	    # cycle 3 : 0b001000
	    # cycle 4 : 0b010000
	    # cycle 5 : 0b010000
	    # cycle 6 : 0b100000
		# cycle 7 : 0b000001
        cs = Signal(6, reset=0b000001)
        # Synchronous assigment
        self.sync += [
            If(self.tick.ce,
                # -- TO BE COMPLETED --
                # [...] rotate cs
                # -- TO BE COMPLETED --
            )
        ]
        # Combinatorial assigment
        self.comb += self.cs.eq(cs)

        # cs to value selection.
        # Here we create a table to translate each of the 8 cs possible values
        # to input value selection.
        # -- TO BE COMPLETED --
        cases = {
            0b000001 : seven_segment.value.eq(self.values[0]),
            # [...]
        }
        # -- TO BE COMPLETED --
        # Combinatorial assigment
        self.comb += Case(self.cs, cases)

# Main ---------------------------------------------------------------------------------------------

if __name__ == '__main__':
    # SevenSegment simulation
    print("SevenSegment simulation")
    dut = SevenSegment()

    def show_seven_segment(abcdefg):
        line0 = ["   ", " _ "]
        line1 = ["   ", "  |", " _ ", " _|", "|  ", "| |" , "|_ ", "|_|"]
        a = abcdefg & 0b1;
        fgb = ((abcdefg >> 1) & 0b001) | ((abcdefg >> 5) & 0b010) | ((abcdefg >> 3) & 0b100)
        edc = ((abcdefg >> 2) & 0b001) | ((abcdefg >> 2) & 0b010) | ((abcdefg >> 2) & 0b100)
        print(line0[a])
        print(line1[fgb])
        print(line1[edc])

    def dut_tb(dut):
        for i in range(16):
            yield dut.value.eq(i)
            yield
            show_seven_segment((yield dut.abcdefg))

    run_simulation(dut, dut_tb(dut), vcd_name="seven_segment.vcd")

    # SevenSegmentDisplay simulation
    print("SevenSegmentDisplay simulation")
    dut = SevenSegmentDisplay(100e6, 0.000001)
    def dut_tb(dut):
        for i in range(4096):
            for j in range(6):
                yield dut.values[j].eq(i + j)
            yield

    run_simulation(dut, dut_tb(dut), vcd_name="display.vcd")
