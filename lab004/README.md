
                  __   ___   ___      ___  ___  ____
                 / /  / _ | / _ )____/ _ \/ _ \/ / /
                / /__/ __ |/ _  /___/ // / // /_  _/
               /____/_/ |_/____/    \___/\___/ /_/
                Use your first FPGA Soft Core CPU

                  FPGA-101 / Lessons / Labs
              Copyright 2018-2020 / EnjoyDigital

[> Presentation / Goals
-----------------------
During this lab, we will create a System on Chip with Migen/LiteX that is
controlled with a Soft Core CPU (VexRiscv).

We will see how to control simple peripherals (Led, Buttons, Switches, PWM, SPI)
from the Soft Core CPU.

For this tutorial, we will need Migen and LiteX. If not install on your computer,
you can get them with the ./litex_setup.py init install --user.


[> Instructions
---------------
1) Build the design and load it.
2) Compile the CPU firmware:
  - cd firmware && make all
3) Start the LiteX Terminal:
  - python3(.6) lxterm /dev/ttyUSBX --kernel firmware/firmware.bin
4) Verify that you are able to interact with the CPU (help for available commands)
and test the display and led.
5) Create a switches_test that recopie the values of the 16 switches to the 16
leds of the board, add it the available commands and help. The list of registers
and accesses functions can be found in build/software/include/generated/csr.h
6) Create a knight rider "knight rider" animation on the 16 leds. (You can
find some inspiration here...: https://www.youtube.com/watch?v=oDhnfajh_w4)
7) Adapt the ADXL362SPI class from test_adxl362.py from Lab003 to C:
  - create 2 separate functions:
    static void adxl362_write(unsigned char addr, unsigned char value);
    static unsigned char adxl362_read(unsigned char addr);
  - create a adxl362_dump function, add it to the available commands and verify
  that you are able to dump the registers.
8) Create a adxl362_test that retrieves the XDATA, YDATA, ZDATA of the ADXL362
accelerometer, converts them to integer (if (value & 0x80): value -= 256), prints
them on the console. Find X axis, Y axis and Z axis of the board.

9) Associate each of the XDATA, YDATA, ZDATA with the R, G, B pwm width of the RGB
led and see if it behaves as expected.

[> Infos
--------
To load the firmware to the board:
lxterm /dev/ttyUSBX --kernel firmware/firmware.bin
then enter "reboot" or press cpu_reset button.

While generating the desing, LiteX generate a csr.h that will be used to
know the available peripherals and their address. This file is located in
build/software/include/generated/csr.h You can open to get the name of the
registers you want to access.
