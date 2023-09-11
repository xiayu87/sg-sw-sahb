import sys
from parameters import *
from datetime import datetime


def gen_blkicd_sp(ins, g):
    stdout_orig = sys.stdout
    if prt == 'single':
        out_file = "output/SAHB_SWITCH_TOP." + str(f_ext)
        sys.stdout = open(str(out_file), 'a')
    else:
        out_file = "output/BLKICD" + str(ins) + "_1X." + str(f_ext)
        sys.stdout = open(str(out_file), 'w')

    sys.stdout.write("** BLKICD" + str(ins) + "_1X\n")
    sys.stdout.write("** Spice file generated using python on " + str(datetime.today()))
    sys.stdout.write("\n")
    ind = int(ins/g)
    sys.stdout.write("include \"~/python/SAHB_LIB_PY/STDAND" + str(g) + "_1X." + str(f_ext) + "\"\n")
    # sys.stdout.write("** beginning of pull-up network ** \n")
    sys.stdout.write("subckt " + "BLKICD" + str(ins) + "_1X")

    for br in range(0, ins):
        sys.stdout.write(" I" + str(br))
    for br in range(0, 4):
        sys.stdout.write(" OUT" + str(br))

    sys.stdout.write(" VDD GND \n")

    #count=0
    #for br in range(0, ins/4):
    #sys.stdout.write("STDAND4_1X icd_nand_0 I0 I1 I2 I3 OUT0\n")
    #sys.stdout.write("STDAND4_1X icd_nand_1 I4 I5 I6 I7 OUT1\n")
    #sys.stdout.write("STDAND4_1X icd_nand_2 I8 I9 I10 I11 OUT2\n")
    #sys.stdout.write("STDAND4_1X icd_nand_3 I12 I13 I14 I15 OUT3\n")

    gt = 0
    bd = int(ins/g)

    for br in range(bd):
        sys.stdout.write("icd_and_" + str(br) + " (")
        for bs in range(g):
            sys.stdout.write(" I" + str(gt))
            gt = gt + 1
        sys.stdout.write(" OUT" + str(br))
        sys.stdout.write(" VDD GND ) STDAND" + str(g) + "_1X" + "\n")

    sys.stdout.write("ends BLKICD" + str(ins) + "_1X \n\n")

    sys.stdout.close()
    sys.stdout = stdout_orig

    return