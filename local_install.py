import os

# clean
os.system("rm -rf migen")
os.system("rm -rf litex")
os.system("rm -rf litedram")

# install migen
os.system("git clone http://github.com/m-labs/migen")
os.system("mv migen migen_tmp")
os.system("mv migen_tmp/migen migen")
os.system("rm -rf migen_tmp")

# install litex
os.system("git clone http://github.com/enjoy-digital/litex --recursive")
os.system("mv litex litex_tmp")
os.system("mv litex_tmp/litex litex")
os.system("rm -rf litex_tmp")
os.system("cp litex/soc/tools/remote/litex_server.py litex_server.py")
os.system("cp litex/soc/tools/litex_term.py litex_term.py")

# install litedram
os.system("git clone http://github.com/enjoy-digital/litedram")
os.system("mv litedram litedram_tmp")
os.system("mv litedram_tmp/litedram litedram")
os.system("rm -rf litedram_tmp")

# install lm32
os.system("wget http://www.das-labor.org/files/madex/lm32_linux_i386.tar.bz2")
os.system("tar -xvjf lm32_linux_i386.tar.bz2")
os.system("rm -rf ~/lm32-toolchain/")
os.system("mv lm32 ~/lm32-toolchain")
os.system("echo 'export PATH=~/lm32-toolchain/bin/:$PATH' >> ~/.bashrc")
