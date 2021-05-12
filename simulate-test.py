#!/usr/bin/env python3

import pexpect
import sys
import time
from ptyprocess import PtyProcessUnicode

f = open("jonesforth.f", 'r').read()
chop = 1
parts = [f[i:i+chop] for i in range(0, len(f), chop)]

def interact():
    child = pexpect.spawn('./sim.sh')
    child.logfile = open("sim.log", "wb")
    child.expect('Liftoff.*===-')
    time.sleep(2)

    for part in parts:
        child.send(part)
        time.sleep(0.0001)
        sys.stdout.flush()

    child.interact()

interact()