Import("env")
import os
import sys
from shutil import copyfile
my_flags = env.ParseFlags(env['BUILD_FLAGS'])

#print(env.Dump())
print(my_flags.get("CPPDEFINES"))

