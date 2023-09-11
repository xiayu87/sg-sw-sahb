import sys
from ran_gen import *
from parameters import *
from datetime import datetime

def gen_fb_sp(ins, outs, h):
    stdout_orig = sys.stdout
    if prt == 'single':
        out_file = "output/SAHB_SWITCH_TOP." + str(f_ext)
        sys.stdout = open(str(out_file), 'a')
    else:
        out_file = "output/SAHBFB" + str(ins) + "x" + str(outs) + "_" + str(h) + "X." + str(f_ext)
        sys.stdout = open(str(out_file), 'w')

    sys.stdout.write("** SAHBFB" + str(ins) + "x" + str(outs) + "_" + str(h) + "X")
    sys.stdout.write("\n")
    sys.stdout.write("** Spice file generated using python on " + str(datetime.today()))
    sys.stdout.write("\n")
    #sys.stdout.write("** beginning of pull-up network ** \n")
    sys.stdout.write("subckt " + "SAHBFB" + str(ins) + "x" + str(outs) + "_" + str(h) + "X")
    for i in range(0, ins):
        sys.stdout.write(" L" + str(i) + " NL" + str(i))
    for i in range(0, ins):
        sys.stdout.write(" S" + str(i) + " NS" + str(i))
    for i in range(0, outs):
        sys.stdout.write(" E" + str(i) + " NE" + str(i))
    for i in range(0, ins):
        sys.stdout.write(" RACK" + str(i) + " NRACK" + str(i))
    for i in range(0, outs):
        sys.stdout.write(" R" + str(i) + " NR" + str(i))
    sys.stdout.write(" NVAL_Lx NVAL_S VDD_L GND")
    sys.stdout.write("\n\n")

    #sys.stdout.write("NM_V_LS1 w_r_ls NRACK VDD_L GND " + str(nmos) + " w=" + str(int(nm_sw)*h) + "n l=" + str(ms_sl) + "n \n")
    for br in range(0, ins):
        sys.stdout.write("NM_V_NR" + str(id_gen()) + " (" + " w" + str(br) + "_nra_l" + " NRACK" + str(br) + " VDD_L" + " GND " + ") " + str(nmos) + " w=" + str(int(nm_sw)*h) + "n l=" + str(ms_sl) + "n \n")

        for bs in range(0, ins):

            sys.stdout.write("NM_NR_L" + str(id_gen()) + " (" + " w" + str(br) + "_nra_l" + " L" + str(br) + " w" + str(br) + "_l" + str(bs) + "_s" + str(bs) + " GND " + ") " + str(nmos) + " w=" + str(int(nm_sw)*h) + "n l=" + str(ms_sl) + "n \n")
            sys.stdout.write("NM_LX_E" + str(id_gen()) + " (" + " w" + str(br) + "_l" + str(bs) + "_s" + str(bs) + " S" + str(br) + " w" + str(br) + "_s_e" + str(br) + " GND " + ") " + str(nmos) + " w=" + str(int(nm_sw)*h) + "n l=" + str(ms_sl) + "n \n")

        sys.stdout.write("NM_E_R" + str(id_gen()) + " (" + " w" + str(br) + "_s_e" + str(br) + " L" + str(br) + " w" + str(br) + "_e" + str(br) + "_r" + str(br) + " GND " + ") " + str(nmos) + " w=" + str(int(nm_sw)*h) + "n l=" + str(ms_sl) + "n \n")

        sys.stdout.write("NM_INV_U" + str(id_gen()) + " (" + " w" + str(br) + "_e" + str(br) + "_r" + str(br) + " NR" + str(br) + " R" + str(br) + " GND " + ") " + str(nmos) + " w=" + str(int(nm_sw)*h) + "n l=" + str(ms_sl) + "n \n")
        sys.stdout.write("NM_INV_D" + str(id_gen()) + " (" + " R" + str(br) + " NR" + str(br) + " w" + str(br) + "_r" + str(br) + "_dn" + str(br) + " GND " + ") " + str(nmos) + " w=" + str(int(nm_sw)*h) + "n l=" + str(ms_sl) + "n \n")

        sys.stdout.write("NM_INV_NE" + str(id_gen()) + " (" + " w" + str(br) + "_r" + str(br) + "_dn" + str(br) + " NE" + str(br) + " GND" + " GND " + ") " + str(nmos) + " w=" + str(int(nm_sw)*h) + "n l=" + str(ms_sl) + "n \n")


        sys.stdout.write("NM_INV_NL" + str(id_gen()) + " (" + " w" + str(br) + "_r" + str(br) + "_dn" + str(br) + " NL0" + " w" + str(br) + "_nl0_nl1" + " GND " + ") " + str(nmos) + " w=" + str(int(nm_sw)*h) + "n l=" + str(ms_sl) + "n \n")
        sys.stdout.write("NM_INV_NLS" + str(id_gen()) + " (" + " w" + str(br) + "_r" + str(br) + "_dn" + str(br) + " NS0" + " w" + str(br) + "_ns0_ns1" + " GND " + ") " + str(nmos) + " w=" + str(int(nm_sw)*h) + "n l=" + str(ms_sl) + "n \n")

        for bs in range(1, ins-1):
            sys.stdout.write("NM_INV_NL" + str(id_gen()) + " (" + " w" + str(br) + "_nl" + str(bs-1) + "_nl" + str(bs) + " NL" + str(bs) + " w" + str(br) + "_nl" + str(bs) + "_nl" + str(bs+1) + " GND " + ") " + str(nmos) + " w=" + str(int(nm_sw)*h) + "n l=" + str(ms_sl) + "n \n")
            sys.stdout.write("NM_INV_NLS" + str(id_gen()) + " (" + " w" + str(br) + "_ns" + str(bs-1) + "_ns" + str(bs) + " NS0" + " w" + str(br) + "_ns" + str(bs) + "_ns" + str(bs+1) + " GND " + ") " + str(nmos) + " w=" + str(int(nm_sw)*h) + "n l=" + str(ms_sl) + "n \n")

        sys.stdout.write("NM_INV_NL" + str(id_gen()) + " (" + " w" + str(br) + "_nl" + str(ins-2) + "_nl" + str(ins-1) + " NL" + str(ins-1) + " GND" + " GND " + ") " + str(nmos) + " w=" + str(int(nm_sw)*h) + "n l=" + str(ms_sl) + "n \n")
        sys.stdout.write("NM_INV_NLS" + str(id_gen()) + " (" + " w" + str(br) + "_ns" + str(ins-2) + "_ns" + str(ins-1) + " NS" + str(ins-1) + " GND" + " GND " + ") " + str(nmos) + " w=" + str(int(nm_sw)*h) + "n l=" + str(ms_sl) + "n \n")

        sys.stdout.write("NM_NVS" + str(id_gen()) + " (" + " w_nvs" + str(br) + "_nvl" + str(br) + " NVAL_S" + " GND" + " GND " + ") " + str(nmos) + " w=" + str(int(nm_sw)*h) + "n l=" + str(ms_sl) + "n \n")
        sys.stdout.write("NM_NVX" + str(id_gen()) + " (" + " w_nvl" + str(br) + "_rack" + str(br) + " NVAL_Lx" + " w_nvs" + str(br) + "_nvl" + str(br) + " GND " + ") " + str(nmos) + " w=" + str(int(nm_sw)*h) + "n l=" + str(ms_sl) + "n \n")
        sys.stdout.write("NM_RAC" + str(id_gen()) + " (" + " R" + str(br) + " RACK" + " w_nvl" + str(br) + "_rack" + str(br) + " GND " + ") " + str(nmos) + " w=" + str(int(nm_sw)*h) + "n l=" + str(ms_sl) + "n \n")

        sys.stdout.write(" \n\n")

        #for bm in range(0, outs):
            #sys.stdout.write("NM_RS_INV" + str(br) + str(bm) + " w_rs" + str(bm) + "_inv" + str(bm) + " RS" + str(bm) + " w_l_rs" + str(bm) + " GND " + str(nmos) + " w=" + str(int(nm_sw)*h) + "n l=" + str(ms_sl) + "n \n")
    #sys.stdout.write("** end of pull-up network ** \n")
    #sys.stdout.write("** beginning of pull-down network ** \n")
    #for bd in range(0, outs):



        #for bs in range(1, ins-2):
            #sys.stdout.write("NM_NL" + str(bd) + str(bs) + " w_nl" + str(bs) + "_nl" + str(bs + 1) + " NL" + str(bs) + " w_nl" + str(bs - 1) + "_nl" + str(bs) + " GND " + str(nmos) + " w=" + str(int(nm_sw)*h) + "n l=" + str(ms_sl) + "n \n")
            #sys.stdout.write("NM_NLS" + str(bd) + str(bs) + " w_nls" + str(bs) + "_nls" + str(bs + 1) + " NLS" + str(bs) + " w_nls" + str(bs - 1) + "_nls" + str(bs) + " GND " + str(nmos) + " w=" + str(int(nm_sw)*h) + "n l=" + str(ms_sl) + "n \n")
        #sys.stdout.write("NM_NL" + str(bs) + " GND NL" + str(ins - 1) + " w_nl" + str(ins - 3) + "_nl" + str(ins - 2) + " GND " + str(nmos) + " w=" + str(int(nm_sw)*h) + "n l=" + str(ms_sl) + "n \n")
        #sys.stdout.write("NM_NLS" + str(bs) + " GND NLS" + str(ins - 1) + " w_nls" + str(ins - 3) + "_nls" + str(ins - 2) + " GND " + str(nmos) + " w=" + str(int(nm_sw)*h) + "n l=" + str(ms_sl) + "n \n")
        #sys.stdout.write("NM_NVS" + str(bd) + " GND NVAL_S w_nvs" + str(bd) + "_nvl" + str(bd) + " GND " + str(nmos) + " w=" + str(int(nm_sw)*h) + "n l=" + str(ms_sl) + "n \n")
        #sys.stdout.write("NM_NVX" + str(bd) + " w_nvs" + str(bd) + "_nvl" + str(bd) + " NVAL_Lx w_nvl" + str(bd) + "_rack" + str(bd) + " GND " + str(nmos) + " w=" + str(int(nm_sw)*h) + "n l=" + str(ms_sl) + "n \n")
        #sys.stdout.write("NM_RAC" + str(bd) + " w_nvl" + str(bd) + "_rack" + str(bd) + " RACK R" + str(bd) + " GND " + str(nmos) + " w=" + str(int(nm_sw)*h) + "n l=" + str(ms_sl) + "n \n")
    sys.stdout.write("ends SAHBFB" + str(ins) + "x" + str(outs) + "_" + str(h) + "X \n\n")
    #sys.stdout.write("** end of pull-down network ** \n")
    sys.stdout.close()
    sys.stdout = stdout_orig

    return

def gen_fbc_sp(ins, outs, h):
    stdout_orig = sys.stdout
    if prt == 'single':
        out_file = "output/SAHB_SWITCH_TOP." + str(f_ext)
        sys.stdout = open(str(out_file), 'a')
    else:
        out_file = "output/SAHBFB" + str(ins) + "x" + str(outs) + "_" + str(h) + "X." + str(f_ext)
        sys.stdout = open(str(out_file), 'w')

    sys.stdout.write("** SAHBFB" + str(ins) + "x" + str(outs) + "_" + str(h) + "X")
    sys.stdout.write("\n")
    sys.stdout.write("** Spice file generated using python on " + str(datetime.today()))
    sys.stdout.write("\n")
    #sys.stdout.write("** beginning of pull-up network ** \n")
    sys.stdout.write("subckt " + "SAHBFB" + str(ins) + "x" + str(outs) + "_" + str(h) + "X")
    for i in range(0, ins):
        sys.stdout.write(" L" + str(i) + " NL" + str(i))
    for i in range(0, ins):
        sys.stdout.write(" S" + str(i) + " NS" + str(i))
    for i in range(0, outs):
        sys.stdout.write(" E" + str(i) + " NE" + str(i))
    for i in range(0, ins):
        sys.stdout.write(" RACK" + str(i) + " NRACK" + str(i))
    for i in range(0, outs):
        sys.stdout.write(" R" + str(i) + " NR" + str(i))
    sys.stdout.write(" NVAL_Lx NVAL_S VDD_L GND")
    sys.stdout.write("\n\n")

