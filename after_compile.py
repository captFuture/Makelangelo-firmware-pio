Import("env", "projenv")
import os
import sys
from shutil import copyfile
makelangelo_flags = env.ParseFlags(env['BUILD_FLAGS'])
current_board = env['PIOENV']

firmware_version = env.GetProjectOption("firmware_version")
print(firmware_version)

script_path = os.path.dirname(os.path.realpath('__file__'))
script_dir = os.path.split(script_path)[0]

def before_build(source, target, env):
    print("--------------------------------before_build")
    # do some actions

def after_build(source, target, env):
    print("--------------------------------after_build")
    os.makedirs(script_path+"\\releases\\"+current_board, exist_ok=True)
    copyfile(script_path+"\\.pio\\build\\"+current_board.lower()+"\\firmware.hex", script_path+"\\releases\\"+current_board.lower()+"\\"+firmware_version+"_firmware.hex")

def before_upload(source, target, env):
    print("--------------------------------before_upload")
    # do some actions

def after_upload(source, target, env):
    print("--------------------------------after_upload")
    # do some actions

env.AddPostAction("buildprog", after_build)
env.AddPreAction("buildprog", before_build)
