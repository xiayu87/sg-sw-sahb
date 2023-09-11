from parameters import *
from gen_fb import *
from gen_clsa import *
from gen_nand import *
from gen_and import *
from gen_inv import *
from gen_cel import *
from gen_blkocd import *
from gen_blkicd import *
from gen_blklack import *
from gen_nor import *
from gen_blksecd import *
from gen_blkinv import *
from gen_testbench import *
from gen_switch import *
from update_mos import *

gen_fb_sp       (5,     5,      1)      #generate functional block
gen_clsa_sp     (5,     1,      1)      #generate clsa block
gen_nand_sp     (5,     1)              #generate nand cell
gen_nand_sp     (4,     1)              #generate nand cell
gen_nand_sp     (2,     1)              #generate nand cell
gen_and_sp      (5,     1)              #generate and cell
gen_and_sp      (4,     1)              #generate and cell
gen_and_sp      (2,     1)              #generate and cell
gen_inv_sp      (1)                     #generate inv cell
gen_cel_sp      (1)                     #generate c-element cell
gen_blkocd_sp   (20,    1)              #generate OCD tree
gen_blkicd_sp   (20,    1)              #generate ICD tree
gen_blklack_sp  (20,    1)              #generate LACK tree
gen_nor_sp      (5,     1)              #generate NOR cell
gen_nor_sp      (4,     1)              #generate NOR cell
gen_nor_sp      (2,     1)              #generate NOR cell
gen_blksecd_sp  (5)                    #generate Select/Exit block
gen_blkinv_sp   (1,    1)              #generate inverter block
gen_switch_sp   (5,     5)              #generate switch module
gen_swtestbench (5,     5)              #generate test bench for switch

#update_mos('TBSWITCH5X5.scs')             #make sure the old_pmos/nmos valued updated in parameters.py