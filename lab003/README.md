
                  __   ___   ___      ___  ___  ____
                 / /  / _ | / _ )____/ _ \/ _ \|_  /
                / /__/ __ |/ _  /___/ // / // //_ <
               /____/_/ |_/____/    \___/\___/____/
                Create your first System on Chip

                  FPGA-101 / Lessons / Labs
              Copyright 2018-2020 / EnjoyDigital

[> Presentation / Goals
-----------------------
During this lab, we will create a basic System on Chip with Migen/LiteX  that we
will control from a Host computer over UART.

We will see how to create simple peripherals (Led, Buttons, Switches, PWM, SPI)
and control them directly from the Host computer.

For this tutorial, we will need Migen and LiteX. If not install on your computer,
you can get them with the ./litex_setup.py init install --user.


[> Instructions
---------------
1) Fill the missing part of pwm.py. You can execute pwm.py and look at the
generated .vcd (with gtkwave) to verify it's working correctly.

2) Execute base.py to build the design. Load it with load.py. Identify your COM
port (/dev/ttyUSBX) and start the LiteX Server (see infos) and verify that the
provided test scripts are working. (in test directory)

3) Create a script that recopie the values of the 16 switches to the 16 leds of
the board.

4) Create a script that do a "knight rider" animation on the 16 leds. (You can
find some inspiration here...: https://www.youtube.com/watch?v=oDhnfajh_w4)

5) Create a script that does a equivalent of the Digital Clock we created in last
lab but now with the core of the clock in pure python on the Host and that only
use the FPGA as display. Use test_display.py to understand how to drive the display.

6) Improve 5) by using Right Button to set the minutes/ Left Button to set the
hours / Center Button to reset the clock.

7) Execute adxl362.py and look at the adxl362.pdf datasheet (you'll find it in
datasheet directory or you can google it). Check that the output of adxl362.py is
coherent with the register map of the datasheet (devid and used registers).

8) Create a script that retrieve the XDATA, YDATA, ZDATA of the ADXL362 accelerometer,
converter them to integer (if (value & 0x80): value -= 256), print them on the console
with a 100ms delay. Find X axis, Y axis and Z axis of the board.

9) Improve 8) by displaying hexadecimal values of XDATA, YDATA, ZDATA to the display.
Since you know that gravity acceleration is 9,81 m s−2 or 1g, what is the LSB resolution
of X, Y, Z DATA? Fix the script you created in 8 to display values in g.

10) Associate each of the XDATA, YDATA, ZDATA with the R, G, B pwm width of the RGB
led and see if it behaves as expected.


[> Infos
--------
To communicate with the board over UART, you first need to start the LiteX Server:
litex_server --uart --uart-port=/dev/ttyUSBX

You can then execute your test script, for example:
python3 test_identifier.py
should return something like:
"fpga_id: My first LiteX System On Chip 2018-05-14 08:55:41"

While generating the desing, LiteX generate a csr.csv file that will be used to
know the available peripherals and their address. This file is located in test.
You can open to get the name of the registers you want to access.
