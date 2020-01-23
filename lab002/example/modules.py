from migen import *
from migen.fhdl import verilog


class MySubmodule(Module):
    def __init__(self):
        self.i = Signal(8) # input
        self.o = Signal(8) # output

        # # #

        # combinatorial assignement
        self.comb += self.o.eq(self.i + 1)


class MyModule(Module):
    def __init__(self):
        self.i = Signal(8) # input
        self.o = Signal(8) # output

        # # #

        # create and declare our submodule
        my_submodule = MySubmodule()
        self.submodules += my_submodule

        # combinatorial assignement
        self.comb += [
            my_submodule.i.eq(self.i),
            self.o.eq(my_submodule.o)
        ]

# Create module
module = MyModule()

# Generate verilog
ios = {module.i, module.o}
print(verilog.convert(module, ios))
