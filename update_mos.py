import os
import sys
import fileinput
from parameters import *

def update_mos(filename):
    in_file = "output/" + filename
    f1 = open(str(in_file), 'r')
    out_file = "output/" + filename + "2." + str(f_ext)
    f2 = open(str(out_file), 'w')
    for line in f1:
        f2.write(line.replace(old_pmos, pmos))
    f1.close()
    f2.close()

    in_file = "output/" + filename
    f1 = open(str(in_file), 'r')
    out_file = "output/" + filename + "2." + str(f_ext)
    f2 = open(str(out_file), 'w')
    for line in f1:
        f2.write(line.replace(old_nmos, nmos))
    f1.close()
    f2.close()