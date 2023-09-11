import sys
from parameters import *
from datetime import datetime


def gen_switch_sp(ins, outs):
    stdout_orig = sys.stdout
    if prt == 'single':
        out_file = "output/SAHB_SWITCH_TOP." + str(f_ext)
        sys.stdout = open(str(out_file), 'a')
    else:
        out_file = "output/SAHBSWITCH" + str(ins) + "x" + str(outs) + "_1X." + str(f_ext)
        sys.stdout = open(str(out_file), 'w')

    sys.stdout.write("** SAHBSWITCH" + str(ins) + "x" + str(outs) + "_1X \n")
    sys.stdout.write("** Spice file generated using python on " + str(datetime.today()))
    sys.stdout.write("\n")
    sys.stdout.write("include \"~/python/SAHB_LIB_PY/SAHBFB5x5_1X." + str(f_ext) + "\"\n")
    sys.stdout.write("include \"~/python/SAHB_LIB_PY/SAHBCLSA4x1_1X." + str(f_ext) + "\"\n")
    sys.stdout.write("include \"~/python/SAHB_LIB_PY/BLKINV20_1X." + str(f_ext) + "\"\n")
    sys.stdout.write("include \"~/python/SAHB_LIB_PY/BLKLACK20_1X." + str(f_ext) + "\"\n")
    sys.stdout.write("include \"~/python/SAHB_LIB_PY/BLKSECD10_1X." + str(f_ext) + "\"\n")
    sys.stdout.write("\n")
    sys.stdout.write("subckt " + "SAHBSWITCH" + str(ins) + "x" + str(outs) + "_1X ")

    for br in range(0, ins): #inputs
        for bs in range(0, 4): #rails
            sys.stdout.write(" L" + str(br) + str(bs))
            sys.stdout.write(" NL" + str(br) + str(bs))

    for br in range(0, ins):
        sys.stdout.write(" S" + str(br))
        sys.stdout.write(" NS" + str(br))
        sys.stdout.write(" RACK" + str(br))
        sys.stdout.write(" NRACK" + str(br))

    for br in range(0, ins): #inputs
        for bs in range(0, 4): #rails
            sys.stdout.write(" R" + str(br) + str(bs))
            sys.stdout.write(" NR" + str(br) + str(bs))

    for br in range(0, outs):
        sys.stdout.write(" E" + str(br))
        sys.stdout.write(" NE" + str(br))
        sys.stdout.write(" LACK" + str(br))
        sys.stdout.write(" NLACK" + str(br))

    sys.stdout.write(" LACKS NLACKS VDD VDD_L GND\n")

    #sys.stdout.write("** 0TH RAIL FUNCTIONAL BLOCK\n")
    #sys.stdout.write("SAHBFB5x5_1X inst0THRAIL0 L00 NL00 L10 NL10 L20 NL20 L30 NL30 L40 NL40 S0 NS0 S1 NS1 S2 NS2 S3 NS3 S4 NS4 E0 NE0 E1 NE1 E2 NE2 E3 NE3 E4 NE4 RACK0 NRACK0 RACK1 NRACK1 RACK2 NRACK2 RACK3 NRACK3 RACK4 NRACK4 R00 NR00 R10 NR10 R20 NR20 R30 NR30 R40 NR40 NVAL_L0 NVAL_S VDD_L GND\n\n")
    sys.stdout.write("inst0THRAIL0 (")
    for br in range(0, ins):
        sys.stdout.write(" L" + str(br) + "0")
        sys.stdout.write(" NL" + str(br) + "0")
    for br in range(0, ins):
        sys.stdout.write(" S" + str(br))
        sys.stdout.write(" NS" + str(br))
    for br in range(0, ins):
        sys.stdout.write(" E" + str(br))
        sys.stdout.write(" NE" + str(br))
    for br in range(0, ins):
        sys.stdout.write(" RACK" + str(br))
        sys.stdout.write(" NRACK" + str(br))
    for br in range(0, ins):
        sys.stdout.write(" R" + str(br) + "0")
        sys.stdout.write(" NR" + str(br) + "0")
    sys.stdout.write(" NVAL_L0 NVAL_SE VDD_L GND ) SAHBFB5x5_1X \n\n")

    #sys.stdout.write("** 1TH RAIL FUNCTIONAL BLOCK\n")
    #sys.stdout.write("SAHBFB5x5_1X inst1THRAIL0 L01 NL01 L11 NL11 L21 NL21 L31 NL31 L41 NL41 S0 NS0 S1 NS1 S2 NS2 S3 NS3 S4 NS4 E0 NE0 E1 NE1 E2 NE2 E3 NE3 E4 NE4 RACK0 NRACK0 RACK1 NRACK1 RACK2 NRACK2 RACK3 NRACK3 RACK4 NRACK4 R01 NR01 R11 NR11 R21 NR21 R31 NR31 R41 NR41 NVAL_L1 NVAL_S VDD_L GND\n\n")
    sys.stdout.write("inst1THRAIL0 (")
    for br in range(0, ins):
        sys.stdout.write(" L" + str(br) + "1")
        sys.stdout.write(" NL" + str(br) + "1")
    for br in range(0, ins):
        sys.stdout.write(" S" + str(br))
        sys.stdout.write(" NS" + str(br))
    for br in range(0, ins):
        sys.stdout.write(" E" + str(br))
        sys.stdout.write(" NE" + str(br))
    for br in range(0, ins):
        sys.stdout.write(" RACK" + str(br))
        sys.stdout.write(" NRACK" + str(br))
    for br in range(0, ins):
        sys.stdout.write(" R" + str(br) + "1")
        sys.stdout.write(" NR" + str(br) + "1")
    sys.stdout.write(" NVAL_L1 NVAL_SE VDD_L GND ) SAHBFB5x5_1X \n\n")

    #sys.stdout.write("** 2TH RAIL FUNCTIONAL BLOCK\n")
    #sys.stdout.write("SAHBFB5x5_1X inst2THRAIL0 L02 NL02 L12 NL12 L22 NL22 L32 NL32 L42 NL42 S0 NS0 S1 NS1 S2 NS2 S3 NS3 S4 NS4 E0 NE0 E1 NE1 E2 NE2 E3 NE3 E4 NE4 RACK0 NRACK0 RACK1 NRACK1 RACK2 NRACK2 RACK3 NRACK3 RACK4 NRACK4 R02 NR02 R12 NR12 R22 NR22 R32 NR32 R42 NR42 NVAL_L2 NVAL_S VDD_L GND\n\n")
    sys.stdout.write("inst2NDRAIL0 (")
    for br in range(0, ins):
        sys.stdout.write(" L" + str(br) + "2")
        sys.stdout.write(" NL" + str(br) + "2")
    for br in range(0, ins):
        sys.stdout.write(" S" + str(br))
        sys.stdout.write(" NS" + str(br))
    for br in range(0, ins):
        sys.stdout.write(" E" + str(br))
        sys.stdout.write(" NE" + str(br))
    for br in range(0, ins):
        sys.stdout.write(" RACK" + str(br))
        sys.stdout.write(" NRACK" + str(br))
    for br in range(0, ins):
        sys.stdout.write(" R" + str(br) + "2")
        sys.stdout.write(" NR" + str(br) + "2")
    sys.stdout.write(" NVAL_L2 NVAL_SE VDD_L GND ) SAHBFB5x5_1X \n\n")

    #sys.stdout.write("** 3TH RAIL FUNCTIONAL BLOCK\n")
    #sys.stdout.write("SAHBFB5x5_1X inst3THRAIL0 L03 NL03 L13 NL13 L23 NL23 L33 NL33 L43 NL43 S0 NS0 S1 NS1 S2 NS2 S3 NS3 S4 NS4 E0 NE0 E1 NE1 E2 NE2 E3 NE3 E4 NE4 RACK0 NRACK0 RACK1 NRACK1 RACK2 NRACK2 RACK3 NRACK3 RACK4 NRACK4 R03 NR03 R13 NR13 R23 NR23 R33 NR33 R43 NR43 NVAL_L3 NVAL_S VDD_L GND\n\n")
    sys.stdout.write("inst3RDRAIL0 (")
    for br in range(0, ins):
        sys.stdout.write(" L" + str(br) + "3")
        sys.stdout.write(" NL" + str(br) + "3")
    for br in range(0, ins):
        sys.stdout.write(" S" + str(br))
        sys.stdout.write(" NS" + str(br))
    for br in range(0, ins):
        sys.stdout.write(" E" + str(br))
        sys.stdout.write(" NE" + str(br))
    for br in range(0, ins):
        sys.stdout.write(" RACK" + str(br))
        sys.stdout.write(" NRACK" + str(br))
    for br in range(0, ins):
        sys.stdout.write(" R" + str(br) + "3")
        sys.stdout.write(" NR" + str(br) + "3")
    sys.stdout.write(" NVAL_L3 NVAL_SE VDD_L GND ) SAHBFB5x5_1X \n\n")

    #sys.stdout.write("** CLSA RAIL 00 and 01\n")
    #sys.stdout.write("SAHBCLSA4x1_1X instCLSA00 R00 NR00 NR01 NR01 RACK0 NVAL_L0 NVAL_L1 NVAL_SE VDD GND \n")
    sys.stdout.write("instCLSA00 (")
    for br in range(0, int(ins/2)):
        sys.stdout.write(" R" + "0" + str(br))
        sys.stdout.write(" NR" + "0" + str(br))
    sys.stdout.write(" RACK0 NVAL_L0 NVAL_L1 NVAL_SE VDD GND ) SAHBCLSA4x1_1X  \n")
    #sys.stdout.write("SAHBCLSA4x1_1X instCLSA01 R02 NR02 NR03 NR03 RACK0 NVAL_L2 NVAL_L3 NVAL_SE VDD GND \n\n")
    sys.stdout.write("instCLSA01 (")
    for br in range(int(ins/2), ins-1):
        sys.stdout.write(" R" + "0" + str(br))
        sys.stdout.write(" NR" + "0" + str(br))
    sys.stdout.write(" RACK0 NVAL_L2 NVAL_L3 NVAL_SE VDD GND ) SAHBCLSA4x1_1X  \n\n")

    #sys.stdout.write("** CLSA RAIL 10 and 11\n")
    #sys.stdout.write("SAHBCLSA4x1_1X instCLSA10 R10 NR10 NR11 NR11 RACK1 NVAL_L0 NVAL_L1 NVAL_SE VDD GND \n")
    sys.stdout.write("instCLSA10 (")
    for br in range(0, int(ins / 2)):
        sys.stdout.write(" R" + "1" + str(br))
        sys.stdout.write(" NR" + "1" + str(br))
    sys.stdout.write(" RACK1 NVAL_L0 NVAL_L1 NVAL_SE VDD GND ) SAHBCLSA4x1_1X  \n")
    #sys.stdout.write("SAHBCLSA4x1_1X instCLSA11 R12 NR12 NR13 NR13 RACK1 NVAL_L2 NVAL_L3 NVAL_SE VDD GND \n\n")
    sys.stdout.write("instCLSA11 (")
    for br in range(int(ins / 2), ins-1):
        sys.stdout.write(" R" + "1" + str(br))
        sys.stdout.write(" NR" + "1" + str(br))
    sys.stdout.write(" RACK1 NVAL_L2 NVAL_L3 NVAL_SE VDD GND ) SAHBCLSA4x1_1X  \n\n")

    #sys.stdout.write("** CLSA RAIL 20 and 21\n")
    #sys.stdout.write("SAHBCLSA4x1_1X instCLSA20 R20 NR20 NR21 NR21 RACK2 NVAL_L0 NVAL_L1 NVAL_SE VDD GND \n")
    sys.stdout.write("instCLSA20 (")
    for br in range(0, int(ins / 2)):
        sys.stdout.write(" R" + "2" + str(br))
        sys.stdout.write(" NR" + "2" + str(br))
    sys.stdout.write(" RACK2 NVAL_L0 NVAL_L1 NVAL_SE VDD GND ) SAHBCLSA4x1_1X  \n")
    #sys.stdout.write("SAHBCLSA4x1_1X instCLSA21 R22 NR22 NR23 NR23 RACK2 NVAL_L2 NVAL_L3 NVAL_SE VDD GND \n\n")
    sys.stdout.write("instCLSA21 (")
    for br in range(int(ins / 2), ins-1):
        sys.stdout.write(" R" + "2" + str(br))
        sys.stdout.write(" NR" + "2" + str(br))
    sys.stdout.write(" RACK2 NVAL_L2 NVAL_L3 NVAL_SE VDD GND ) SAHBCLSA4x1_1X  \n\n")

    #sys.stdout.write("** CLSA RAIL 30 and 31\n")
    #sys.stdout.write("SAHBCLSA4x1_1X instCLSA30 R30 NR30 NR31 NR31 RACK3 NVAL_L0 NVAL_L1 NVAL_SE VDD GND \n")
    sys.stdout.write("instCLSA30 (")
    for br in range(0, int(ins / 2)):
        sys.stdout.write(" R" + "3" + str(br))
        sys.stdout.write(" NR" + "3" + str(br))
    sys.stdout.write(" RACK3 NVAL_L0 NVAL_L1 NVAL_SE VDD GND ) SAHBCLSA4x1_1X  \n")
    #sys.stdout.write("SAHBCLSA4x1_1X instCLSA31 R32 NR32 NR33 NR33 RACK3 NVAL_L2 NVAL_L3 NVAL_SE VDD GND \n\n")
    sys.stdout.write("instCLSA31 (")
    for br in range(int(ins / 2), ins-1):
        sys.stdout.write(" R" + "3" + str(br))
        sys.stdout.write(" NR" + "3" + str(br))
    sys.stdout.write(" RACK3 NVAL_L2 NVAL_L3 NVAL_SE VDD GND ) SAHBCLSA4x1_1X  \n\n")

    #sys.stdout.write("** CLSA RAIL 40 and 41\n")
    #sys.stdout.write("SAHBCLSA4x1_1X instCLSA40 R40 NR40 NR41 NR41 RACK4 NVAL_L0 NVAL_L1 NVAL_SE VDD GND \n")
    sys.stdout.write("instCLSA40 (")
    for br in range(0, int(ins / 2)):
        sys.stdout.write(" R" + "4" + str(br))
        sys.stdout.write(" NR" + "4" + str(br))
    sys.stdout.write(" RACK4 NVAL_L0 NVAL_L1 NVAL_SE VDD GND ) SAHBCLSA4x1_1X  \n")
    #sys.stdout.write("SAHBCLSA4x1_1X instCLSA41 R42 NR42 NR43 NR43 RACK4 NVAL_L2 NVAL_L3 NVAL_SE VDD GND \n\n")
    sys.stdout.write("instCLSA41 (")
    for br in range(int(ins / 2), ins-1):
        sys.stdout.write(" R" + "4" + str(br))
        sys.stdout.write(" NR" + "4" + str(br))
    sys.stdout.write(" RACK4 NVAL_L2 NVAL_L3 NVAL_SE VDD GND ) SAHBCLSA4x1_1X  \n\n")

    #sys.stdout.write("** INVERTER BLOCK PLACEMENT\n")
    sys.stdout.write("instBLKINV0 ( R00 NR00 R01 NR01 R02 NR02 R03 NR03 R10 NR10 R11 NR11 R12 NR12 R13 NR13 R20 NR20 R21 NR21 R22 NR22 R23 NR23 R30 NR30 R31 NR31 R32 NR32 R33 NR33 R40 NR40 R41 NR41 R42 NR42 R43 NR43 VDD GND ) BLKINV20_1X \n\n")

    #sys.stdout.write("** LACK BLOCK PLACEMENT\n")
    sys.stdout.write("instBLKLACK0 ( NL00 NL10 NL20 NL30 NL40 NL01 NL11 NL21 NL31 NL41 NL02 NL12 NL22 NL32 NL42 NL03 NL13 NL23 NL33 NL43 NR00 NR01 NR02 NR03 NR10 NR11 NR12 NR13 NR20 NR21 NR22 NR23 NR30 NR31 NR32 NR33 NR40 NR41 NR42 NR43 LACK0 LACK1 LACK2 LACK3 LACK4 NVAL_L0 NVAL_L1 NVAL_L2 NVAL_L3 LACKS VDD GND ) BLKLACK20_1X \n\n")

    #sys.stdout.write("** SECD BLOCK PLACEMENT\n")
    sys.stdout.write("instBLKSECD0 ( S0 S1 S2 S3 S4 E0 E1 E2 E3 E4 NVAL_SE VDD GND ) BLKSECD10_1X \n\n")

    sys.stdout.write("ends SAHBSWITCH5x5_1X \n\n")

    sys.stdout.close()
    sys.stdout = stdout_orig

    return