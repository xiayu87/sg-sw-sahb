import sys
from ran_gen import *
from parameters import *
from datetime import datetime


def gen_nand_sp(ins, h):
    stdout_orig = sys.stdout
    if prt == 'single':
        out_file = "output/SAHB_SWITCH_TOP." + str(f_ext)
        sys.stdout = open(str(out_file), 'a')
    else:
        out_file = "output/STDNAND" + str(ins) + "_" + str(h) + "X." + str(f_ext)
        sys.stdout = open(str(out_file), 'w')

    sys.stdout.write("** STDNAND" + str(ins) + "_" + str(h) + "X")
    sys.stdout.write("\n")
    sys.stdout.write("** Spice file generated using python on " + str(datetime.today()))
    sys.stdout.write("\n")
    # sys.stdout.write("** beginning of pull-up network ** \n")
    sys.stdout.write("subckt " + "STDNAND" + str(ins) + "_" + str(h) + "X ")

    for br in range(0, ins):
        sys.stdout.write(" I" + str(br))
    sys.stdout.write(" OUT VDD GND \n")

    #sys.stdout.write("PM_PU0 OUT I0 VDD VDD " + str(pmos) + " w=" + str(pm_sw * h) + "n l=" + str(ms_sl) + "n \n")

    for br in range(0, ins):
        sys.stdout.write("PM_PU" + str(id_gen()) + " (" + " OUT" + " I" + str(br) + " VDD" + " VDD " + ") " + str(pmos) + " w=" + str(pm_sw * h) + "n l=" + str(ms_sl) + "n \n")
        #sys.stdout.write("PM_PU" + str(br) + " OUT I" + str(br) + " VDD VDD " + str(pmos) + " w=" + str(pm_sw * h) + "n l=" + str(ms_sl) + "n \n")

    sys.stdout.write("NM_PD" + str(id_gen()) + " (" + " OUT" + " I0" + " w_o_0" + " GND " + ") " + str(nmos) + " w=" + str(nm_sw * h) + "n l=" + str(ms_sl) + "n \n")
    for br in range(1, ins-1):
        sys.stdout.write("NM_PD" + str(id_gen()) + " (" + " w_o_" + str(br-1) + " I" + str(br) + " w_o_" + str(br) + " GND " + ") " + str(nmos) + " w=" + str(nm_sw * h) + "n l=" + str(ms_sl) + "n \n")
        #sys.stdout.write("NM_R1" + str(br) + " GND I" + str(br) + " OUT GND " + str(nmos) + " w=" + str(nm_sw * h) + "n l=" + str(ms_sl) + "n \n")

    sys.stdout.write("NM_PD" + str(id_gen()) + " (" + " w_o_" + str(ins-2) + " I" + str(ins-1) + " GND" + " GND " + ") " + str(nmos) + " w=" + str(nm_sw * h) + "n l=" + str(ms_sl) + "n \n")
    sys.stdout.write("ends STDNAND" + str(ins) + "_" + str(h) + "X \n\n")

    sys.stdout.close()
    sys.stdout = stdout_orig

    return