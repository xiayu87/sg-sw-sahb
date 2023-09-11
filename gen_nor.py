import sys
from parameters import *
from datetime import datetime


def gen_nor_sp(ins, h):
    stdout_orig = sys.stdout
    if prt == 'single':
        out_file = "output/SAHB_SWITCH_TOP." + str(f_ext)
        sys.stdout = open(str(out_file), 'a')
    else:
        out_file = "output/STDNOR" + str(ins) + "_" + str(h) + "X." + str(f_ext)
        sys.stdout = open(str(out_file), 'w')

    sys.stdout.write("** STDNOR" + str(ins) + "_" + str(h) + "X")
    sys.stdout.write("\n")
    sys.stdout.write("** Spice file generated using python on " + str(datetime.today()))
    sys.stdout.write("\n")
    # sys.stdout.write("** beginning of pull-up network ** \n")
    sys.stdout.write("subckt " + "STDNOR" + str(ins) + "_" + str(h) + "X ")

    for br in range(0, ins):
        sys.stdout.write(" I" + str(br))
    sys.stdout.write(" OUT VDD GND \n")

    #sys.stdout.write("PM_PU0 OUT I0 VDD VDD " + str(pmos) + " w=" + str(pm_sw * h) + "n l=" + str(ms_sl) + "n \n")

    sys.stdout.write("PM_PU0" + " (" + " w_o_0" + " I0" + " VDD" + " VDD " + ") " + str(pmos) + " w=" + str(int(pm_sw) * 6 * h) + "n l=" + str(ms_sl) + "n \n")
    for br in range(1, ins-1):
        sys.stdout.write("PM_PU" + str(br) + " (" + " w_o_" + str(br) + " I" + str(br) + " w_o_" + str(br-1) + " VDD " + ") " + str(pmos) + " w=" + str(int(pm_sw) * 6 * h) + "n l=" + str(ms_sl) + "n \n")
    sys.stdout.write("PM_PU" + str(ins - 1) + " (" + " OUT" + " I" + str(ins - 1) + " w_o_" + str(ins - 2) + " VDD " + ") " + str(pmos) + " w=" + str(int(pm_sw) * 6 * h) + "n l=" + str(ms_sl) + "n \n")


    for br in range(0, ins):
        sys.stdout.write("NM_PD" + str(br) + " (" + " OUT" + " I" + str(br) + " GND" + " GND " + ") " + str(nmos) + " w=" + str(int(nm_sw) * 3 * h) + "n l=" + str(ms_sl) + "n \n")
        #sys.stdout.write("PM_PU" + str(br) + " OUT I" + str(br) + " VDD VDD " + str(pmos) + " w=" + str(pm_sw * h) + "n l=" + str(ms_sl) + "n \n")

    #sys.stdout.write("NM_PD0 w_o_0 I0 OUT GND " + str(nmos) + " w=" + str(nm_sw * h) + "n l=" + str(ms_sl) + "n \n")
    #for br in range(1, ins-1):
        #sys.stdout.write("NM_PD" + str(br) + " w_o_" + str(br) + " I" + str(br) + " w_o_" + str(br-1) + " GND " + str(nmos) + " w=" + str(nm_sw * h) + "n l=" + str(ms_sl) + "n \n")
        #sys.stdout.write("NM_R1" + str(br) + " GND I" + str(br) + " OUT GND " + str(nmos) + " w=" + str(nm_sw * h) + "n l=" + str(ms_sl) + "n \n")

    #sys.stdout.write("NM_PD" + str(ins-1) + " GND I" + str(ins-1) + " w_o_" + str(ins-2) + " GND " + str(nmos) + " w=" + str(nm_sw * h) + "n l=" + str(ms_sl) + "n \n")
    sys.stdout.write("ends STDNOR" + str(ins) + "_" + str(h) + "X \n\n")

    sys.stdout.close()
    sys.stdout = stdout_orig

    return