import os
os.system("git clone http://github.com/m-labs/migen")
os.system("mv migen migen_tmp")
os.system("mv migen_tmp/migen migen")
os.system("rm -rf migen_tmp")