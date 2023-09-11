import sys
from ran_gen import *
from parameters import *
from datetime import datetime


def gen_clsa_sp(ins, orl, h):
    stdout_orig = sys.stdout
    if prt == 'single':
        out_file = "output/SAHB_SWITCH_TOP." + str(f_ext)
        sys.stdout = open(str(out_file), 'a')
    else:
        out_file = "output/SAHBCLSA" + str(ins) + "x" + str(orl) + "_" + str(h) + "X." + str(f_ext)
        sys.stdout = open(str(out_file), 'w')

    sys.stdout.write("** SAHBCLSA" + str(ins) + "x" + str(orl) + "_" + str(h) + "X")
    sys.stdout.write("\n")
    sys.stdout.write("** Spice file generated using python on " + str(datetime.today()))
    sys.stdout.write("\n")
    # sys.stdout.write("** beginning of pull-up network ** \n")
    sys.stdout.write("subckt " + "SAHBCLSA" + str(ins) + "x" + str(orl) + "_" + str(h) + "X")
    #sys.stdout.write(" RACK" + str(i) + " NRACK" + str(i))
    #for j in range(0, 3):
        #for i in range(0, orl):
    sys.stdout.write(" R0 NR0 R1 NR1 RACK NVAL0 NVAL1 NVALS VDD GND \n")

    sys.stdout.write("PM_NVAL0l" + " (" + " w_nval_nvals" + " NVAL0" + " VDD" + " VDD" + " ) " + str(pmos) + " w=" + str(int(pm_sw) * 4 * h) + "n l=" + str(ms_sl) + "n \n")
    sys.stdout.write("PM_NVAL1l" + " (" + " w_nval_nvals" + " NVAL1" + " VDD" + " VDD" + " ) " + str(pmos) + " w=" + str(int(pm_sw) * 4 * h) + "n l=" + str(ms_sl) + "n \n")
    sys.stdout.write("PM_NVALSl" + " (" + " w_nvals_rack" + " NVALS" + " VDD" + " VDD" + " ) " + str(pmos) + " w=" + str(int(pm_sw) * 4 * h) + "n l=" + str(ms_sl) + "n \n")
    sys.stdout.write("PM_RACK0l" + " (" + " w_rack_r" + " RACK" + " w_nval_nvals" + " VDD" + " ) " + str(pmos) + " w=" + str(int(pm_sw) * 4 * h) + "n l=" + str(ms_sl) + "n \n")

    sys.stdout.write("PM_NVAL0r" + " (" + " w_blk_nr" + " NVAL0" + " VDD" + " VDD" + " ) " + str(pmos) + " w=" + str(pm_sw * h) + "n l=" + str(ms_sl) + "n \n")
    sys.stdout.write("PM_NVAL1r" + " (" + " w_blk_nr" + " NVAL1" + " VDD" + " VDD" + " ) " + str(pmos) + " w=" + str(pm_sw * h) + "n l=" + str(ms_sl) + "n \n")
    sys.stdout.write("PM_NVALSr" + " (" + " w_blk_nr" + " NVALS" + " VDD" + " VDD" + " ) " + str(pmos) + " w=" + str(pm_sw * h) + "n l=" + str(ms_sl) + "n \n")
    sys.stdout.write("PM_RACK0r" + " (" + " w_blk_nr" + " RACK" + " VDD" + " VDD" + " ) " + str(pmos) + " w=" + str(pm_sw * h) + "n l=" + str(ms_sl) + "n \n")

    sys.stdout.write("PM_NR0" + " (" + " w_rack_r" + " NR0" + " w_blk_nr" + " VDD" + " ) " + str(pmos) + " w=" + str(pm_sw * h) + "n l=" + str(ms_sl) + "n \n")
    sys.stdout.write("PM_NR1" + " (" + " w_rack_r" + " NR1" + " w_blk_nr" + " VDD" + " ) " + str(pmos) + " w=" + str(pm_sw * h) + "n l=" + str(ms_sl) + "n \n")

    sys.stdout.write("PM_R0" + " (" + " R1" + " R0" + " w_rack_r" + " VDD" + " ) " + str(pmos) + " w=" + str(int(pm_sw) * 4 * h) + "n l=" + str(ms_sl) + "n \n")
    sys.stdout.write("PM_R1" + " (" + " R0" + " R1" + " w_rack_r" + " VDD" + " ) " + str(pmos) + " w=" + str(int(pm_sw) * 4 * h) + "n l=" + str(ms_sl) + "n \n")
    sys.stdout.write("NM_R0" + " (" + " R1" + " R0" + " GND" + " GND" + " ) " + str(nmos) + " w=" + str(int(nm_sw) * 4 * h) + "n l=" + str(ms_sl) + "n \n")
    sys.stdout.write("NM_R1" + " (" + " R0" + " R1" + " GND" + " GND" + " ) " + str(nmos) + " w=" + str(int(nm_sw) * 4 * h) + "n l=" + str(ms_sl) + "n \n")

    sys.stdout.write("ends SAHBCLSA" + str(ins) + "x" + str(orl) + "_" + str(h) + "X \n\n")

    sys.stdout.close()
    sys.stdout = stdout_orig

    return