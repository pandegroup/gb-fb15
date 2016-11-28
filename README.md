# gb-fb15
For the MD simulation of liquid-crystalline DPPC bilayers.

![alt tag](https://raw.githubusercontent.com/pandegroup/gb-fb15/master/vis/ic.png)


### GMX simulation
1 ns of NPT dynamics, assuming you are in the root of this repository and GMX is in your PATH

```bash
cd gromacs
grompp -f npt.mdp -c ic.gro -p lipid.top -o ic_npt.tpr
mdrun -deffnm ic_npt
```
### Details
10.1021/acs.jctc.6b00801
