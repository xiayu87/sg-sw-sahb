import sys
from parameters import *
from datetime import datetime


def gen_blksecd_sp(ins):
    stdout_orig = sys.stdout
    if prt == 'single':
        out_file = "output/SAHB_SWITCH_TOP." + str(f_ext)
        sys.stdout = open(str(out_file), 'a')
    else:
        out_file = "output/BLKSECD" + str(ins) + "_1X." + str(f_ext)
        sys.stdout = open(str(out_file), 'w')

    ins_d = int(ins / 2)
    sys.stdout.write("** BLKSECD" + str(ins) + "_1X\n")
    sys.stdout.write("** Spice file generated using python on " + str(datetime.today()))
    sys.stdout.write("\n")
    sys.stdout.write("include \"~/python/SAHB_LIB_PY/STDNOR" + str(ins_d) + "_1X." + str(f_ext) + "\"\n")
    sys.stdout.write("include \"~/python/SAHB_LIB_PY/STDNOR2_1X." + str(f_ext) + "\"\n")
    sys.stdout.write("include \"~/python/SAHB_LIB_PY/STDNOR4_1X." + str(f_ext) + "\"\n")
    # sys.stdout.write("** beginning of pull-up network ** \n")
    sys.stdout.write("subckt " + "BLKSECD" + str(ins) + "_1X")

    for br in range(0, ins):
        sys.stdout.write(" I" + str(br))
    sys.stdout.write(" OUT VDD GND \n")


    sys.stdout.write("inst_scd_0 (")
    for br in range(0, int(ins_d)):
        sys.stdout.write(" I" + str(br))
    sys.stdout.write(" w_scd_0 VDD GND ) STDNOR" + str(ins_d) + "_1X  \n")

    sys.stdout.write("inst_scd_1 (")
    for br in range(int(ins_d), int(ins)):
        sys.stdout.write(" I" + str(br))
    sys.stdout.write(" w_scd_1 VDD GND ) STDNOR" + str(ins_d) + "_1X  \n")

    sys.stdout.write("inst_ecd_0 (")
    for br in range(0, int(ins_d)):
        sys.stdout.write(" I" + str(br))
    sys.stdout.write(" w_ecd_0 VDD GND ) STDNOR" + str(ins_d) + "_1X  \n")

    sys.stdout.write("inst_ecd_1 (")
    for br in range(0, int(ins_d)):
        sys.stdout.write(" I" + str(br))
    sys.stdout.write(" w_ecd_1 VDD GND ) STDNOR" + str(ins_d) + "_1X  \n")

    #if ins == 8:
    #    sys.stdout.write("STDNOR4_1X inst_scd_0 I0 I1 I2 I3 w_scd_0 \n")
    #    sys.stdout.write("STDAND4_1X inst_ecd_0 I4 I5 I6 I7 w_ecd_0 \n")
    #elif ins == 10:
    #    sys.stdout.write("STDNOR5_1X inst_scd_0 I0 I1 I2 I3 I4 w_scd_0 \n")
    #    sys.stdout.write("STDAND5_1X inst_ecd_0 I5 I6 I7 I8 I9 w_ecd_0 \n")

    sys.stdout.write("inst_scd_a ( w_scd_0 w_scd_0 w_scd_out_0 VDD GND ) STDNOR2_1X \n")
    sys.stdout.write("inst_scd_b ( w_scd_1 w_scd_1 w_scd_out_1 VDD GND ) STDNOR2_1X \n")
    sys.stdout.write("inst_ecd_c ( w_ecd_0 w_ecd_0 w_ecd_out_2 VDD GND ) STDNOR2_1X \n")
    sys.stdout.write("inst_ecd_d ( w_ecd_1 w_ecd_1 w_ecd_out_3 VDD GND ) STDNOR2_1X \n")

    sys.stdout.write("inst_out_0 ( w_scd_out_0 w_scd_out_1 w_ecd_out_0 w_ecd_out_1 OUT VDD GND ) STDNOR4_1X \n")

    sys.stdout.write("ends BLKSECD" + str(ins) + "_1X \n")

    sys.stdout.close()
    sys.stdout = stdout_orig

    return
