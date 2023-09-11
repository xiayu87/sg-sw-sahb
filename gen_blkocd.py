import sys
from parameters import *
from datetime import datetime


def gen_blkocd_sp(ins, g):
    stdout_orig = sys.stdout
    if prt == 'single':
        out_file = "output/SAHB_SWITCH_TOP." + str(f_ext)
        sys.stdout = open(str(out_file), 'a')
    else:
        out_file = "output/BLKOCD" + str(ins) + "_1X." + str(f_ext)
        sys.stdout = open(str(out_file), 'w')

    sys.stdout.write("** BLKOCD" + str(ins) + "_1X\n")
    sys.stdout.write("** Spice file generated using python on " + str(datetime.today()))
    sys.stdout.write("\n")
    sys.stdout.write("include \"~/python/SAHB_LIB_PY/STDNAND" + str(g) + "_1X." + str(f_ext) + "\"\n")
    sys.stdout.write("include \"~/python/SAHB_LIB_PY/STDNAND" + str(2) + "_1X." + str(f_ext) + "\"\n")
    # sys.stdout.write("** beginning of pull-up network ** \n")
    sys.stdout.write("subckt " + "BLKOCD" + str(ins) + "_1X")

    for br in range(0, ins):
        sys.stdout.write(" I" + str(br))
    sys.stdout.write(" OUT VDD GND \n")

    #count=0
    #for br in range(0, ins/4):
    #sys.stdout.write("STDAND4_1X ocd_nand_0 I0 I1 I2 I3 w_nand_0\n")
    #sys.stdout.write("STDAND4_1X ocd_nand_1 I4 I5 I6 I7 w_nand_1\n")
    #sys.stdout.write("STDAND4_1X ocd_nand_2 I8 I9 I10 I11 w_nand_2\n")
    #sys.stdout.write("STDAND4_1X ocd_nand_3 I12 I13 I14 I15 w_nand_3\n")

    #sys.stdout.write("STDAND2_1X ocd_nand_m0 w_nand_0 w_nand_0 w_nand_f0\n")
    #sys.stdout.write("STDAND2_1X ocd_nand_m1 w_nand_1 w_nand_1 w_nand_f1\n")
    #sys.stdout.write("STDAND2_1X ocd_nand_m2 w_nand_2 w_nand_2 w_nand_f2\n")
    #sys.stdout.write("STDAND2_1X ocd_nand_m3 w_nand_3 w_nand_3 w_nand_f3\n")

    #sys.stdout.write("STDAND4_1X ocd_nand_f w_nand_f0 w_nand_f1 w_nand_f2 w_nand_f3 OUT\n")

    gt = 0
    bd = int(ins / g)

    for br in range(bd):
        sys.stdout.write("ocd_nand_i" + str(br) + " (")
        for bs in range(g):
            sys.stdout.write(" I" + str(gt) + " ")
            gt = gt + 1
        sys.stdout.write(" w_nand_i" + str(br) + " VDD GND ) STDNAND" + str(g) + "_1X  \n")

    gt = 0
    for br in range(g-1):
        sys.stdout.write("ocd_nand_m" + str(br) + " (")
        for bs in range(2):
            sys.stdout.write(" w_nand_i" + str(gt) + " ")
        gt = gt + 1
        sys.stdout.write(" w_nand_m" + str(br) + " VDD GND ) STDNAND" + str(2) + "_1X  \n")

    gt = 0
    sys.stdout.write("ocd_nand_f0 (")
    for br in range(g):
        sys.stdout.write(" w_nand_m" + str(br) + " ")
        gt = gt + 1
    sys.stdout.write(" OUT VDD GND ) STDNAND" + str(g) + "_1X \n")

    sys.stdout.write("ends BLKOCD" + str(ins) + "_1X \n\n")

    sys.stdout.close()
    sys.stdout = stdout_orig

    return