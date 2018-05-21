import os

# install migen
os.system("git clone http://github.com/m-labs/migen")
os.system("mv migen migen_tmp")
os.system("mv migen_tmp/migen migen")
os.system("rm -rf migen_tmp")

# install litex
os.system("git clone http://github.com/enjoy-digital/litex")
os.system("mv litex litex_tmp")
os.system("mv litex_tmp/litex litex")
os.system("rm -rf litex_tmp")
os.system("cp litex/soc/tools/remote/litex_server.py litex_server.py")

# install litedram
os.system("git clone http://github.com/enjoy-digital/litedram")
os.system("mv litedram litedram_tmp")
os.system("mv litedram_tmp/litedram litedram")
os.system("rm -rf litedram_tmp")

