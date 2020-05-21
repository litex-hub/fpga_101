#!/usr/bin/env python3

from migen import *

from litex.build.generic_platform import *
from litex.build.xilinx import XilinxPlatform

from litex.soc.integration.soc_core import *
from litex.soc.integration.builder import *
from litex.soc.cores.uart import UARTWishboneBridge
from litex.soc.cores import dna, xadc
from litex.soc.cores.spi import SPIMaster

from ios import Led, RGBLed, Button, Switch
from display import SevenSegmentDisplay

# IOs ----------------------------------------------------------------------------------------------

_io = [
    ("user_led",  0, Pins("H17"), IOStandard("LVCMOS33")),
    ("user_led",  1, Pins("K15"), IOStandard("LVCMOS33")),
    ("user_led",  2, Pins("J13"), IOStandard("LVCMOS33")),
    ("user_led",  3, Pins("N14"), IOStandard("LVCMOS33")),
    ("user_led",  4, Pins("R18"), IOStandard("LVCMOS33")),
    ("user_led",  5, Pins("V17"), IOStandard("LVCMOS33")),
    ("user_led",  6, Pins("U17"), IOStandard("LVCMOS33")),
    ("user_led",  7, Pins("U16"), IOStandard("LVCMOS33")),
    ("user_led",  8, Pins("V16"), IOStandard("LVCMOS33")),
    ("user_led",  9, Pins("T15"), IOStandard("LVCMOS33")),
    ("user_led", 10, Pins("U14"), IOStandard("LVCMOS33")),
    ("user_led", 11, Pins("T16"), IOStandard("LVCMOS33")),
    ("user_led", 12, Pins("V15"), IOStandard("LVCMOS33")),
    ("user_led", 13, Pins("V14"), IOStandard("LVCMOS33")),
    ("user_led", 14, Pins("V12"), IOStandard("LVCMOS33")),
    ("user_led", 15, Pins("V11"), IOStandard("LVCMOS33")),

    ("user_sw",  0, Pins("J15"), IOStandard("LVCMOS33")),
    ("user_sw",  1, Pins("L16"), IOStandard("LVCMOS33")),
    ("user_sw",  2, Pins("M13"), IOStandard("LVCMOS33")),
    ("user_sw",  3, Pins("R15"), IOStandard("LVCMOS33")),
    ("user_sw",  4, Pins("R17"), IOStandard("LVCMOS33")),
    ("user_sw",  5, Pins("T18"), IOStandard("LVCMOS33")),
    ("user_sw",  6, Pins("U18"), IOStandard("LVCMOS33")),
    ("user_sw",  7, Pins("R13"), IOStandard("LVCMOS33")),
    ("user_sw",  8, Pins("T8"), IOStandard("LVCMOS33")),
    ("user_sw",  9, Pins("U8"), IOStandard("LVCMOS33")),
    ("user_sw", 10, Pins("R16"), IOStandard("LVCMOS33")),
    ("user_sw", 11, Pins("T13"), IOStandard("LVCMOS33")),
    ("user_sw", 12, Pins("H6"), IOStandard("LVCMOS33")),
    ("user_sw", 13, Pins("U12"), IOStandard("LVCMOS33")),
    ("user_sw", 14, Pins("U11"), IOStandard("LVCMOS33")),
    ("user_sw", 15, Pins("V10"), IOStandard("LVCMOS33")),

    ("user_btn", 0, Pins("N17"), IOStandard("LVCMOS33")),
    ("user_btn", 1, Pins("P18"), IOStandard("LVCMOS33")),
    ("user_btn", 2, Pins("P17"), IOStandard("LVCMOS33")),
    ("user_btn", 3, Pins("M17"), IOStandard("LVCMOS33")),
    ("user_btn", 4, Pins("M18"), IOStandard("LVCMOS33")),

    ("user_rgb_led", 0,
        Subsignal("r", Pins("N16")),
        Subsignal("g", Pins("R11")),
        Subsignal("b", Pins("G14")),
        IOStandard("LVCMOS33"),
    ),

    ("display_cs_n",  0, Pins("J17 J18 J14 P14 K2 U13 T9 T14"), IOStandard("LVCMOS33")),
    ("display_abcdefg",  0, Pins("T10 R10 K16 K13 P15 T11 L18 H15"), IOStandard("LVCMOS33")),

    ("clk100", 0, Pins("E3"), IOStandard("LVCMOS33")),

    ("cpu_reset", 0, Pins("C12"), IOStandard("LVCMOS33")),

    ("serial", 0,
        Subsignal("tx", Pins("D4")),
        Subsignal("rx", Pins("C4")),
        IOStandard("LVCMOS33"),
    ),

    ("adxl362_spi", 0,
        Subsignal("cs_n", Pins("D15")),
        Subsignal("clk", Pins("F15")),
        Subsignal("mosi", Pins("F14")),
        Subsignal("miso", Pins("E15")),
        IOStandard("LVCMOS33")
    ),

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

# Create our soc (fpga description)
class BaseSoC(SoCMini):
    def __init__(self, platform, **kwargs):
        sys_clk_freq = int(100e6)

        # SoCMini (No CPU, we are controlling the SoC over UART)
        SoCMini.__init__(self, platform, sys_clk_freq, csr_data_width=32,
            ident="My first LiteX System On Chip", ident_version=True)

        # Clock Reset Generation
        self.submodules.crg = CRG(platform.request("clk100"), ~platform.request("cpu_reset"))

        # No CPU, use Serial to control Wishbone bus
        self.submodules.serial_bridge = UARTWishboneBridge(platform.request("serial"), sys_clk_freq)
        self.add_wb_master(self.serial_bridge.wishbone)

        # FPGA identification
        self.submodules.dna = dna.DNA()
        self.add_csr("dna")

        # FPGA Temperature/Voltage
        self.submodules.xadc = xadc.XADC()
        self.add_csr("xadc")

        # Led
        user_leds = Cat(*[platform.request("user_led", i) for i in range(16)])
        self.submodules.leds = Led(user_leds)
        self.add_csr("leds")

        # Switches
        user_switches = Cat(*[platform.request("user_sw", i) for i in range(16)])
        self.submodules.switches = Switch(user_switches)
        self.add_csr("switches")

        # Buttons
        user_buttons = Cat(*[platform.request("user_btn", i) for i in range(5)])
        self.submodules.buttons = Button(user_buttons)
        self.add_csr("buttons")

        # RGB Led
        self.submodules.rgbled  = RGBLed(platform.request("user_rgb_led",  0))
        self.add_csr("rgbled")

        # Accelerometer
        self.submodules.adxl362 = SPIMaster(platform.request("adxl362_spi"),
            data_width   = 32,
            sys_clk_freq = sys_clk_freq,
            spi_clk_freq = 1e6)
        self.add_csr("adxl362")

        # SevenSegmentDisplay
        self.submodules.display = SevenSegmentDisplay(sys_clk_freq)
        self.add_csr("display")
        self.comb += [
            platform.request("display_cs_n").eq(~self.display.cs),
            platform.request("display_abcdefg").eq(~self.display.abcdefg)
        ]

soc = BaseSoC(platform)

# Build --------------------------------------------------------------------------------------------

builder = Builder(soc, output_dir="build", csr_csv="test/csr.csv")
builder.build(build_name="top")
