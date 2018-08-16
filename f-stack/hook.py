#!/usr/bin/env python

import os
import sys

from subprocess import call

lib = sys.argv[1]

print("Hooking {}".format(lib))

syms_file = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), "syms")
with open(syms_file, 'r') as fs:
    for sym in fs:
        sym = sym.strip()
        call(['objcopy', '--redefine-sym', '{0}=ff_{0}'.format(sym), lib])
