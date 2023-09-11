import sys
from config import *
from parameters import *    

def gen_swtestbench(ins, outs):
    sys.stdout.write("Printing test bench spectre file \n")
    stdout_pointer = sys.stdout

    with open('./output/SWTESTBENCH.' + str(f_ext), 'w') as _file:
        sys.stdout = _file
        sys.stdout.write("// Generated for: spectre \n")
        sys.stdout.write("simulator lang=spectre \n")
        sys.stdout.write("global 0 \n")
        sys.stdout.write("include \"/netstorage/soft2/technology/SMIC28PS/pdk/oa/SPDK28LL_10518_OA_CDS_V1.1/smic28ll_10518_oa_cds_v1.1/models/spectre/l0028ll_v1p1_3r_spe.lib\" section=tt \n")
        sys.stdout.write("include \"/netstorage/soft2/technology/SMIC28PS/pdk/oa/SPDK28LL_10518_OA_CDS_V1.1/smic28ll_10518_oa_cds_v1.1/models/spectre/l0028ll_v1p1_3r_spe.lib\" section=ldmos_tt \n")
        sys.stdout.write("include \"/netstorage/soft2/technology/SMIC28PS/pdk/oa/SPDK28LL_10518_OA_CDS_V1.1/smic28ll_10518_oa_cds_v1.1/models/spectre/l0028ll_v1p1_3r_spe.lib\" section=bjt_tt \n")
        sys.stdout.write("include \"/netstorage/soft2/technology/SMIC28PS/pdk/oa/SPDK28LL_10518_OA_CDS_V1.1/smic28ll_10518_oa_cds_v1.1/models/spectre/l0028ll_v1p1_3r_spe.lib\" section=dio_tt \n")
        sys.stdout.write("include \"/netstorage/soft2/technology/SMIC28PS/pdk/oa/SPDK28LL_10518_OA_CDS_V1.1/smic28ll_10518_oa_cds_v1.1/models/spectre/l0028ll_v1p1_3r_spe.lib\" section=res_tt \n")
        sys.stdout.write("include \"/netstorage/soft2/technology/SMIC28PS/pdk/oa/SPDK28LL_10518_OA_CDS_V1.1/smic28ll_10518_oa_cds_v1.1/models/spectre/l0028ll_v1p1_3r_spe.lib\" section=var_tt \n")
        sys.stdout.write("include \"/netstorage/soft2/technology/SMIC28PS/pdk/oa/SPDK28LL_10518_OA_CDS_V1.1/smic28ll_10518_oa_cds_v1.1/models/spectre/l0028ll_v1p1_3r_spe.lib\" section=mom_tt \n")
        sys.stdout.write("include \"~/python/SAHB_LIB_PY/SAHBSWITCH5x5_1X." + str(f_ext) + "\" \n")
        sys.stdout.write("\n\n\n")
        sys.stdout.write("// Cell name: SWTESTBENCH \n")
        sys.stdout.write("// View name: schematic \n")

        sys.stdout.write("INST_SWITCH (")
        for br in range(0, ins):  # inputs
            for bs in range(0, 4):  # rails
                sys.stdout.write(" L" + str(br) + str(bs))
                sys.stdout.write(" NL" + str(br) + str(bs))

        for br in range(0, ins):
            sys.stdout.write(" S" + str(br))
            sys.stdout.write(" NS" + str(br))
            sys.stdout.write(" RACK" + str(br))
            sys.stdout.write(" NRACK" + str(br))

        for br in range(0, ins):  # inputs
            for bs in range(0, 4):  # rails
                sys.stdout.write(" R" + str(br) + str(bs))
                sys.stdout.write(" NR" + str(br) + str(bs))

        for br in range(0, outs):
            sys.stdout.write(" E" + str(br))
            sys.stdout.write(" NE" + str(br))
            sys.stdout.write(" LACK" + str(br))
            sys.stdout.write(" NLACK" + str(br))

        sys.stdout.write(" LACKS NLACKS VDD VDD_L GND) SAHBSWITCH5x5_1X \n\n")

        for br in range(0, ins):
            for bs in range(0, 4):
                if dL[br] == 0:
                    _dL = dh + str(0)
                    _dnL = dl + str(1)
                else:
                    _dL = dl + str(1)
                    _dnL = dh + str(0)

                if dS[br] == 0:
                    _dS = dl + str(0)
                    _dnS = dh + str(1)
                else:
                    _dS = dh + str(1)
                    _dnS = dl + str(0)

                if dE[br] == 0:
                    _dE = dl + str(0)
                    _dnE = dh + str(1)
                else:
                    _dE = dh + str(1)
                    _dnE = dl + str(0)

                sys.stdout.write("vL" + str(br) + str(bs) + " (L" + str(br) + str(bs) + " 0) vsource type=bit period=" + str(per) + str(per_ts) + " rise=" + str(rise) + str(rise_ts) + " fall=" + str(fall) + str(fall_ts) + " data=\"" + str(_dL) + "\" rptstart=" + str(repeat) + " rpttimes=" + str(repeat_t) + "\n")
                sys.stdout.write("vNL" + str(br) + str(bs) + " (NL" + str(br) + str(bs) + " 0) vsource type=bit period=" + str(per) + str(per_ts) + " rise=" + str(rise) + str(rise_ts) + " fall=" + str(fall) + str(fall_ts) + " data=\"" + str(_dnL) + "\" rptstart=" + str(repeat) + " rpttimes=" + str(repeat_t) + "\n")


            sys.stdout.write("vRACK" + str(br) + " (RACK" + str(br) + " 0) vsource type=bit period=" + str(per) + str(per_ts) + " rise=" + str(rise) + str(rise_ts) + " fall=" + str(fall) + str(fall_ts) + " data=\"")

            for ar in range(0, ins):
                sys.stdout.write(str(dR[br][ar]))

            sys.stdout.write("\" rptstart=" + (repeat) + " rpttimes=" + str(repeat_t) + "\n")
            sys.stdout.write("vNRACK" + str(br) + " (NRACK" + str(br) + " 0) vsource type=bit period=" + str(per) + str(per_ts) + " rise=" + str(rise) + str(rise_ts) + " fall=" + str(fall) + str(fall_ts) + " data=\"")

            for ar in range(0, ins):
                sys.stdout.write(str(dnR[br][ar]))

            sys.stdout.write("\" rptstart=" + (repeat) + " rpttimes=" + str(repeat_t) + "\n")

            sys.stdout.write("vS" + str(br) + " (S" + str(br) + " 0) vsource type=bit period=" + str(per) + str(per_ts) + " rise=" + str(rise) + str(rise_ts) + " fall=" + str(fall) + str(fall_ts) + " data=\"" + str(_dS) + "\" rptstart=" + str(repeat) + " rpttimes=" + str(repeat_t) + "\n")
            sys.stdout.write("vNS" + str(br) + " (NS" + str(br) + " 0) vsource type=bit period=" + str(per) + str(per_ts) + " rise=" + str(rise) + str(rise_ts) + " fall=" + str(fall) + str(fall_ts) + " data=\"" + str(_dnS) + "\" rptstart=" + str(repeat) + " rpttimes=" + str(repeat_t) + "\n")

            sys.stdout.write("vE" + str(br) + " (E" + str(br) + " 0) vsource type=bit period=" + str(per) + str(per_ts) + " rise=" + str(rise) + str(rise_ts) + " fall=" + str(fall) + str(fall_ts) + " data=\"" + str(_dE) + "\" rptstart=" + str(repeat) + " rpttimes=" + str(repeat_t) + "\n")
            sys.stdout.write("vNE" + str(br) + " (NE" + str(br) + " 0) vsource type=bit period=" + str(per) + str(per_ts) + " rise=" + str(rise) + str(rise_ts) + " fall=" + str(fall) + str(fall_ts) + " data=\"" + str(_dnE) + "\" rptstart=" + str(repeat) + " rpttimes=" + str(repeat_t) + "\n")

        #sys.stdout.write("V1 (VDD 0) vsource dc=1 type=dc \n")
        #sys.stdout.write("V0 (VDD_L 0) vsource dc=350.00m type=dc \n")
        sys.stdout.write("V0 (VDD 0) vsource dc=1.05 type=dc \n")
        sys.stdout.write("V1 (VDD_L 0) vsource dc=350.00m type=dc \n")
        sys.stdout.write("V2 (GND 0) vsource dc=0 type=dc \n")

        sys.stdout.write("simulatorOptions options reltol=1e-3 vabstol=1e-6 iabstol=1e-12 temp=" + str(temp) + " \\ \n\ttnom=27 scalem=1.0 scale=0.9 gmin=1e-14 rforce=1 maxnotes=5 maxwarns=5 \\ \n\tdigits=5 cols=80 pivrel=1e-3 sensfile=\"../psf/sens.output\" \\ \n\tchecklimitdest=psf \n")
        sys.stdout.write("tran tran stop=" + str(trans_time) + str(trans_ts) + " errpreset=conservative write=\"spectre.ic\" \\ \n\twritefinal=\"spectre.fc\" annotate=status maxiters=5 \n")
        sys.stdout.write("finalTimeOP info what=oppoint where=rawfile \n")
        sys.stdout.write("modelParameter info what=models where=rawfile \n")
        sys.stdout.write("element info what=inst where=rawfile \n")
        sys.stdout.write("outputParameter info what=output where=rawfile \n")
        sys.stdout.write("designParamVals info what=parameters where=rawfile \n")
        sys.stdout.write("primitives info what=primitives where=rawfile \n")
        sys.stdout.write("subckts info what=subckts where=rawfile \n")
        sys.stdout.write("saveOptions options save=allpub \n\n")

        sys.stdout = stdout_pointer
    return