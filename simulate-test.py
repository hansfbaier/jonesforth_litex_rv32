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
    #child.close()

def test():
    p = PtyProcessUnicode.spawn(['./sim.sh'])
    while True:
        l = p.readline()
        print(str(l))
        if  "Liftoff" in l:
            print("GOT IT")
            break

    n = p.write("42 EMIT ")
    print(p.read(n + 1))
    time.sleep(1)
    p.close()

interact()