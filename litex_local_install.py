import os
os.system("git clone http://github.com/enjoy-digital/litex")
os.system("mv litex litex_tmp")
os.system("mv litex_tmp/litex litex")
os.system("rm -rf litex_tmp")
os.system("cp litex/soc/tools/remote/litex_server.py litex_server.py")

os.system("git clone http://github.com/enjoy-digital/litedram")
os.system("mv litedram litedram_tmp")
os.system("mv litedram_tmp/litedram litedram")
os.system("rm -rf litedram_tmp")