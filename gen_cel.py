import sys
from parameters import *
from datetime import datetime


def gen_cel_sp(h):
    stdout_orig = sys.stdout
    if prt == 'single':
        out_file = "output/SAHB_SWITCH_TOP." + str(f_ext)
        sys.stdout = open(str(out_file), 'a')
    else:
        out_file = "output/STDCEL2_" + str(h) + "X." + str(f_ext)
        sys.stdout = open(str(out_file), 'w')

    sys.stdout.write("** STDCEL2" + "_" + str(h) + "X \n")
    sys.stdout.write("** Spice file generated using python on " + str(datetime.today()))
    sys.stdout.write("\n")
    # sys.stdout.write("** beginning of pull-up network ** \n")
    sys.stdout.write("subckt " + "STDCEL2_" + str(h) + "X ")

    sys.stdout.write(" I0 I1 OUT NOUT VDD GND \n")

    sys.stdout.write("PM_CEL0" + "(" + " w_uk0" + " I0" + " VDD" + " VDD " + ") " + str(pmos) + " w=" + str(pm_sw * h) + "n l=" + str(ms_sl) + "n \n")
    sys.stdout.write("PM_CEL1" + "(" + " w_uk1" + " I0" + " VDD" + " VDD " + ") " + str(pmos) + " w=" + str(pm_sw * h) + "n l=" + str(ms_sl) + "n \n")
    sys.stdout.write("PM_CEL2" + "(" + " w_uk1" + " I1" + " VDD" + " VDD " + ") " + str(pmos) + " w=" + str(pm_sw * h) + "n l=" + str(ms_sl) + "n \n")

    sys.stdout.write("PM_CEL3" + "(" + " NOUT" + " I1" + " w_uk0" + " VDD " + ") " + str(pmos) + " w=" + str(pm_sw * h) + "n l=" + str(ms_sl) + "n \n")
    sys.stdout.write("PM_CEL4" + "(" + " NOUT" + " OUT" + " w_uk1" + " VDD " + ") " + str(pmos) + " w=" + str(pm_sw * h) + "n l=" + str(ms_sl) + "n \n")

    sys.stdout.write("PM_INV" + "(" + " OUT" + " NOUT" + " VDD" + " VDD " + ") " + str(pmos) + " w=" + str(pm_sw * h) + "n l=" + str(ms_sl) + "n \n")
    sys.stdout.write("NM_INV" + "(" + " OUT" + " NOUT" + " GND" + " GND " + ") " + str(nmos) + " w=" + str(nm_sw * h) + "n l=" + str(ms_sl) + "n \n")

    sys.stdout.write("NM_CEL0" + "(" + " NOUT" + " I1" + " w_uk2" + " GND " + ") " + str(nmos) + " w=" + str(nm_sw * h) + "n l=" + str(ms_sl) + "n \n")
    sys.stdout.write("NM_CEL1" + "(" + " NOUT" + " OUT" + " w_uk3" + " GND " + ") " + str(nmos) + " w=" + str(nm_sw * h) + "n l=" + str(ms_sl) + "n \n")

    sys.stdout.write("NM_CEL2" + "(" + " w_uk2" + " I0" + " GND" + " GND " + ") " + str(nmos) + " w=" + str(nm_sw * h) + "n l=" + str(ms_sl) + "n \n")
    sys.stdout.write("NM_CEL3" + "(" + " w_uk3" + " I1" + " GND" + " GND " + ") " + str(nmos) + " w=" + str(nm_sw * h) + "n l=" + str(ms_sl) + "n \n")
    sys.stdout.write("NM_CEL4" + "(" + " w_uk3" + " I0" + " GND" + " GND " + ") " + str(nmos) + " w=" + str(nm_sw * h) + "n l=" + str(ms_sl) + "n \n")

    sys.stdout.write("ends STDCEL2_" + str(h) + "X \n\n")

    sys.stdout.close()
    sys.stdout = stdout_orig

    return