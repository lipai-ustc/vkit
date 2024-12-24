# vkit (for generating VASP input files)
lipai@mail.ustc.edu.cn  
A python tool for generating VASP inputs for general tasks.  POSCAR file should be prepared in advance.

Installation
```
echo "export PATH=$PATH:#The vkit PATH" >> ~/.bashrc
echo "export VASP_PP_PATH=#Your POTCARs PATH" >> ~/.bashrc
```
remember to replace the "#The vkit PATH" and "#Your POTCARs PATH" with your correct PATHs.
The "#Your POTCARs PATH" should contain folders "potpaw_LDA" and "potpaw_PBE" containing availabe elemental POTCAR files.

Options
```
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  --ref                 add suffix '_ref' for all output files
  -p, --wpotcar         write POTCAR based on the exist POSCAR
  --lda                 if use this option, POTCARs from 'potpaw_LDA' will be used.
                        default: use POTCARs from 'potpaw_PBE'
  --ppath=PPATH         PPATH is a pseudopotential folder path. 
                        default: $VASP_PP_PATH
  --paccu=PACCU         PACCU can be 'Normal' or 'Low'.
                        'Normal' for recommend pp [https://www.vasp.at/wiki/index.php/Choosing_pseudopotentials]
                        'Low' for POTCARs without suffix
                        default: Normal
  -k, --wkpoints        write KPOINTS
  --ktype=KTYPE         KTYPE can be 'G' or 'M', corresponding to Gamma centered and normal MP kpoint sampling methods, respectively.
                        default: G
  --dim=DIM             periodic condiction for x/y/z (0-no,1-yes). 3 values
                        should be provided for 3 directions
                        default: 1 1 1
  --kaccu=KACCU         kpoint spacing in 2*Pi A^-1.
                        default: 0.25
  -i, --wincar          write INCAR
  --accu=ACCU           ACCU can be 'A' for Accurate, 'N' for normal, 'L' for low
                        default: 'A' for DOS/workfunction/phonon calculations, otherwise 'N'
  --opt                 perform optimization calculation
  --optaccu             opt with high accuracy: EDIFFG=-0.01
  --md                  perform MD calculation
  --ML                  perform ML calculation
  --dos                 perform dos calculation
  --workfunction        perform workfunction calculation
  --bader               perform bader calculation
  --ELF                 perform ELF calculation
  --spin                control ISPIN only
  --pbeU                perform PBE+U calculation
  --mix                 AMIX/BMIX for convergence
  --chout               output CHGCAR and WAVECAR
                        default: do not write CHGCAR and WAVECAR files
  --r2scan              use R2SCAN functional
  --addcharge=ADDCHARGE
                        add negative charge. >0 (<0) means add (remove) electron.
  --STM                 STM simulation calculations
  --BKcharge            specific Band/Kpoint charge density
  --phonon              DFPT method to calculate force constant
  --vibration           vibration of molecule or adsorbates
  --neb                 NEB calculation
```

Examples 1
```
python ../../vkit -i -k -p --dim=1 1 0 --STM
```
-i -k -p     # for generating INCAR KPOINTS and POTCAR
--dim=1 1 0  # for slab model calculation, where the number of kpoints in z direction is set to 1.
--STM        # write into INCAR STM-simulation related tags, such as LPARD, LSEPK, LSEPB, NBMOD, and EINT

Example 2
```
python ../../vkit -i -k -p --opt --accu=Low --dim=1 1 0
```
--opt        # write into INCAR optimization related tags, such as ISIF, IBRION, POTIM, EDIFFG and NSW

Example 3
```
python ../../vkit -i -k -p --spin --dim=1 1 0 --dos
```
--spin       # write into INCAR open-shell related tags, such as ISPIN, MAGMOM, and set NELM=200
--dos        # write into INCAR density-of-state related tags, such as ISMEAR, LORBIT, NEDOS, EMIN, and EMAX

Example 4
```
python ../../vkit -i -k -p --spin --r2scan --pbeU --dim=1 1 0
```
--r2scan     # write into INCAR r2scan related tags, such as METAGGA, and LASPH
--pbeU       # write into INCAR PBE+U related tags, such as LDAU, LDAUTYPE, LDAUL, LDAUU, and LDAUJ

More examples can be found in the 'examples' folder.
