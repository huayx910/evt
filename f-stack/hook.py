#!/usr/bin/env python

import os
import sys

from subprocess import call

symlist = os.environ['FF_PATH'] + '/lib/ff_api.symlist'
lib = sys.argv[1]

print("Hooking {}".format(lib))

with open(symlist, 'r') as fs:
    for sym in fs:
    	s = sym[3:]
        call(['objcopy', '--redefine-sym', '{0}=ff_{0}'.format(s), lib])
