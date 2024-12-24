# vkit (vasp-kit)
lipai@mail.ustc.edu.cn  
A python tool for generating VASP inputs for general tasks.  
Usage please refer to the file *test.sh* in the *example* folder.

```
rm {0..9}*/* -r

for i in 0.all 1.normal  2.opt  3.spin  4.r2scan  5.pbeU  6.args_opt_dos  7.args_opt_phonon  8.args_opt_vibration 9*
do
    cp POSCAR $i
done

cd 0.all
python ../../vkit -i -k -p --dim=1 1 0 --opt --md --ML --Econverge --dos --workfunction --bader --ELF --spin --pbeU --mix --chout --r2scan --addcharge 2.3 --STM --BKcharge --phonon --vibration

cd ../1.normal
python ../../vkit -i -k -p --dim=1 1 0 --STM

cd ../2.opt
python ../../vkit -i -k -p --opt --accu=Low --dim=1 1 0

cd ../3*
python ../../vkit -i -k -p --spin --dim=1 1 0 --dos

cd ../4*
python ../../vkit -i -k -p --spin --r2scan --dim=1 1 0

cd ../5*
python ../../vkit -i -k -p --spin --r2scan --pbeU --dim=1 1 0

cd ../6*
python ../../vkit opt dos --dim=1 1 0

cd ../7*
python ../../vkit opt phonon --dim=1 1 0

cd ../8*
python ../../vkit opt vibration --dim=1 1 0

cd ../9.spin+pbeU+args_opt_dos
python ../../vkit opt dos --spin --pbeU  --dim=1 1 0
```
