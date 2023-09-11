import sys
from parameters import *
from datetime import datetime


def gen_blkinv_sp(ins, g):
    stdout_orig = sys.stdout
    if prt == 'single':
        out_file = "output/SAHB_SWITCH_TOP." + str(f_ext)
        sys.stdout = open(str(out_file), 'a')
    else:
        out_file = "output/BLKINV" + str(ins) + "_1X." + str(f_ext)
        sys.stdout = open(str(out_file), 'w')

    sys.stdout.write("** BLKINV" + str(ins) + "_1X\n")
    sys.stdout.write("** Spice file generated using python on " + str(datetime.today()))
    sys.stdout.write("\n")
    sys.stdout.write("include \"~/python/SAHB_LIB_PY/STDINV_1X." + str(f_ext) + "\"\n")
    # sys.stdout.write("** beginning of pull-up network ** \n")
    sys.stdout.write("subckt " + "BLKINV" + str(ins) + "_" + "1X")

    for br in range(0, ins):
        sys.stdout.write(" R" + str(br) + " NR" + str(br))

    sys.stdout.write(" VDD GND \n")

    gt = 0
    bd = int(ins/g)

    for br in range(0, g):
        for bs in range(0, 4):
            sys.stdout.write("instBLKINV" + str(br) + str(bs) + " ( R" + str(br) + str(bs) + " NR" + str(br) + str(bs) + " VDD GND ) STDINV_1X "+ " \n")

    sys.stdout.write("ends BLKINV" + str(ins) + "_1X \n\n")

    sys.stdout.close()
    sys.stdout = stdout_orig

    return