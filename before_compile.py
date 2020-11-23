Import("env")
import os
import sys
from shutil import copyfile
makelangelo_flags = env.ParseFlags(env['BUILD_FLAGS'])
print(env['PIOENV'])
#print(env.Dump())

script_path = os.path.dirname(os.path.realpath('__file__'))
script_dir = os.path.split(script_path)[0]

current_board = env['PIOENV']

if current_board.upper() == "RUMBA":
    copyfile(script_path+"\\configs\\local_rumba_config.h", script_path+"\\Makelangelo-firmware\\local_config.h")
    print("------------------------------- COMPILING FOR "+current_board)
elif current_board.upper() == "RAMPS":
    copyfile(script_path+"\\configs\\local_ramps_config.h", script_path+"\\Makelangelo-firmware\\local_config.h")
elif current_board.upper() == "MKS":
    copyfile(script_path+"\\configs\\local_mks_config.h", script_path+"\\Makelangelo-firmware\\local_config.h")
elif current_board.upper() == "SANGUINOLULU":
    copyfile(script_path+"\\configs\\local_sanguinolulu_config.h", script_path+"\\Makelangelo-firmware\\local_config.h")
elif current_board.upper() == "SIXI_MEGA":
    copyfile(script_path+"\\configs\\local_sixi_mega_config.h", script_path+"\\Makelangelo-firmware\\local_config.h")
else:
    copyfile(script_path+"\\configs\\local_config.h", script_path+"\\Makelangelo-firmware\\local_config.h")
    print("------------------------------- COMPILING FALLBACK")
