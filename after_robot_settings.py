Import("env", "projenv")
import os
import sys
from shutil import copyfile
my_flags = env.ParseFlags(env['BUILD_FLAGS'])

#print(env.Dump())
print(my_flags.get("CPPDEFINES"))

def before_upload(source, target, env):
    print("--------------------------------before_upload")
    # do some actions

def after_upload(source, target, env):
    print("--------------------------------after_upload")
    # do some actions

env.AddPostAction("buildprog", before_upload)
env.AddPostAction("buildprog", after_upload)
