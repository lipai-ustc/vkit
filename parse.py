import os, re
from optparse import OptionParser

############################################################
__version__ = '1.0'
pi=3.14159265
############################################################

def command_line_arg():
    usage = "usage: %prog [options] arg1 arg2"
    par = OptionParser(usage=usage, version=__version__)

    par.add_option('--ref',  action='store_true',
                   default=False, help='add suffix \'_ref\' for all output files')

    # POTCAR related
    par.add_option('-p', '--wpotcar', action='store_true',
                   default=False, help='write POTCAR based on the exist POSCAR')

    par.add_option( '--lda', action='store_true',
                   default=False, help='use LDA pseudopotential, otherwise use PBE')

    par.add_option( '--ppath', action='store',type='string',
                   default=None, help='pseudopotential folder path. Default: $VASP_PP_PATH')

    par.add_option('--paccu', action='store',type='string',
                   default='Normal', help='\'Normal\' for recommend pp, \'Low\' without setups ')

    # KPOINTS related
    par.add_option('-k', '--wkpoints', action='store_true',
                   default=False, help='write KPOINTS')

    par.add_option('--ktype', action='store',type='string',
                   default='Gamma', help='kpoint sampling type')

    par.add_option('--dim', action='store', type='int',nargs=3,
                   default=(1,1,1), help='periodic condiction for x/y/z (0-no,1-yes). 3 values should be provided for 3 directions')

    par.add_option('--kaccu', action='store', type='float',default=None,
                   help='kpoint spacing in 2*Pi A^-1.')

    # INCAR related
    par.add_option('-i', '--wincar', action='store_true', default=False, 
                   help='write INCAR')

    par.add_option('--accu', action='store', default=None,type='string',
                   help='perform optimization calculation')

    par.add_option('--opt', action='store_true', default=False,
                   help='perform optimization calculation')

    par.add_option('--optaccu', action='store_true', default=False,
                   help='opt with high accuracy: EDIFFG=-0.01')

    par.add_option('--md', action='store_true', default=False,
                   help='perform MD calculation')

    par.add_option('--ML', action='store_true', default=False,
                   help='perform ML calculation')

    par.add_option('--Econverge', action='store_true', default=False,
                   help='perform ML calculation')

    par.add_option('--dos', action='store_true', default=False,
                   help='perform dos calculation')

    par.add_option('--workfunction', action='store_true', default=False,
                   help='perform workfunction calculation')

    par.add_option('--bader', action='store_true', default=False,
                   help='perform bader calculation')

    par.add_option('--ELF', action='store_true', default=False,
                   help='perform ELF calculation')

    par.add_option('--spin', action='store_true', default=False,
                   help='control ISPIN only')

    par.add_option('--pbeU', action='store_true', default=False,
                   help='perform PBE+U calculation')

    par.add_option('--mix', action='store_true', default=False,
                   help='AMIX/BMIX for convergence')

    par.add_option('--chout', action='store_true', default=False,
                   help='output CHGCAR and WAVECAR')

    par.add_option('--r2scan', action='store_true', default=False,
                   help='use R2SCAN functional')

    par.add_option('--addcharge', action='store', default=0, type='float',
                   help='add negative charge. >0 (<0) means add (remove) electron.')

    par.add_option('--STM', action='store_true', default=False,
                   help='STM simulation')

    par.add_option('--BKcharge', action='store_true', default=False,
                   help='specific Band/Kpoint charge density')

    par.add_option('--phonon', action='store_true', default=False,
                   help='DFPT method to calculate force constant')

    par.add_option('--vibration', action='store_true', default=False,
                   help='vibration of molecule or adsorbates')

    par.add_option('--neb', action='store_true', default=False,
                   help='NEB calculation')

    return par.parse_args()

if(__name__=='__main__'):
    opts, args = command_line_arg()
    print(type(opts))
    print("opts   ",opts)
    print("args   ",args)
