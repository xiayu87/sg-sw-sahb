import sys
from parameters import *
from datetime import datetime


def gen_blklack_sp(ins, g):
    stdout_orig = sys.stdout
    if prt == 'single':
        out_file = "output/SAHB_SWITCH_TOP." + str(f_ext)
        sys.stdout = open(str(out_file), 'a')
    else:
        out_file = "output/BLKLACK" + str(ins) + "_1X." + str(f_ext)
        sys.stdout = open(str(out_file), 'w')

    sys.stdout.write("** BLKLACK" + str(ins) + "_1X\n")
    sys.stdout.write("** Spice file generated using python on " + str(datetime.today()))
    sys.stdout.write("\n")
    sys.stdout.write("include \"~/python/SAHB_LIB_PY/BLKICD" + str(ins) + "_1X." + str(f_ext) + "\"\n")
    sys.stdout.write("include \"~/python/SAHB_LIB_PY/BLKOCD" + str(ins) + "_1X." + str(f_ext) + "\"\n")
    sys.stdout.write("include \"~/python/SAHB_LIB_PY/STDCEL2_1X." + str(f_ext) + "\"\n")
    # sys.stdout.write("** beginning of pull-up network ** \n")
    sys.stdout.write("subckt " + "BLKLACK" + str(ins) + "_1X")

    for br in range(0, ins):
        sys.stdout.write(" ICD" + str(br))
    for br in range(0, ins):
        sys.stdout.write(" OCD" + str(br))
    for br in range(0, g):
        sys.stdout.write(" LACK" + str(br))
    #for br in range(0, g):
        #sys.stdout.write(" NVAL_L" + str(br))

    sys.stdout.write(" NVAL_L0 NVAL_L1 NVAL_L2 NVAL_L3 LACKS VDD GND \n")

    #count=0
    #for br in range(0, ins/4):

    gt = g
    sys.stdout.write("inst_icd_0 (")
    for br in range(0, ins):
        sys.stdout.write(" ICD" + str(br) + " ")
        gt = gt + 1

    for br in range(0, g-1):
        sys.stdout.write(" NVAL_L" + str(br))
    sys.stdout.write(" VDD GND ) BLKICD" + str(ins) + "_1X  \n")

    gt = g
    sys.stdout.write("inst_ocd_0 (")
    for br in range(0, ins):
        sys.stdout.write(" OCD" + str(br))
        gt = gt + 1

    sys.stdout.write(" LACKS")
    sys.stdout.write(" VDD GND ) BLKOCD" + str(ins) + "_1X \n")


    #sys.stdout.write("BLKICD inst_icd_0 ICD0 ICD1 ICD2 ICD3 ICD4 ICD5 ICD6 ICD7 ICD8 ICD9 ICD10 ICD11 ICD12 ICD13 ICD14 ICD15 p_icd_0 p_icd_1 p_icd_2 p_icd_3\n")
    #sys.stdout.write("BLKOCD inst_ocd_1 OCD0 OCD1 OCD2 OCD3 OCD4 OCD5 OCD6 OCD7 OCD8 OCD9 OCD10 OCD11 OCD12 OCD13 OCD14 OCD15 LACKS \n")

    for br in range (0, g-1):
        sys.stdout.write("inst_cel_" + str(br) + " ( NVAL_L" + str(br) + " LACKS LACK" + str(br) + " disc_" + str(br) + " VDD GND ) STDCEL2_1X \n")

    #sys.stdout.write("\nSTDCEL2_1X inst_cel_0 p_icd_0 LACKS LACK0 \n")
    #sys.stdout.write("STDCEL2_1X inst_cel_1 p_icd_1 LACKS LACK1 \n")
    #sys.stdout.write("STDCEL2_1X inst_cel_2 p_icd_2 LACKS LACK2 \n")
    #sys.stdout.write("STDCEL2_1X inst_cel_3 p_icd_3 LACKS LACK3 \n")


    sys.stdout.write("ends BLKLACK" + str(ins) + "_1X \n\n")

    sys.stdout.close()
    sys.stdout = stdout_orig

    return