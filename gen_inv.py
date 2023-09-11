import sys
from parameters import *
from datetime import datetime


def gen_inv_sp(h):
    stdout_orig = sys.stdout
    if prt == 'single':
        out_file = "output/SAHB_SWITCH_TOP." + str(f_ext)
        sys.stdout = open(str(out_file), 'a')
    else:
        out_file = "output/STDINV_" + str(h) + "X." + str(f_ext)
        sys.stdout = open(str(out_file), 'w')

    sys.stdout.write("** STDINV" + "_" + str(h) + "X")
    sys.stdout.write("\n")
    sys.stdout.write("** Spice file generated using python on " + str(datetime.today()))
    sys.stdout.write("\n")
    # sys.stdout.write("** beginning of pull-up network ** \n")
    sys.stdout.write("subckt " + "STDINV_" + str(h) + "X ")

    sys.stdout.write(" I OUT VDD GND \n")

    sys.stdout.write("PM_INV ( OUT I VDD VDD ) " + str(pmos) + " w=" + str(int(pm_sw) * h * 2) + "n l=" + str(ms_sl) + "n \n")
    sys.stdout.write("NM_INV ( OUT I GND GND ) " + str(nmos) + " w=" + str(int(nm_sw) * h * 2) + "n l=" + str(ms_sl) + "n \n")

    sys.stdout.write("ends STDINV_" + str(h) + "X \n\n")

    sys.stdout.close()
    sys.stdout = stdout_orig

    return