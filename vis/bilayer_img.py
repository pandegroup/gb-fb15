import os
from chimera import runCommand as rc 
from chimera import replyobj 

gro_file = '../gromacs/ic.gro'
rc('open ' + gro_file)
rc("preset apply publication 1")
rc("light mode ambient")
rc("rep bs")
rc("setattr m stickScale .2")
rc("setattr m ballScale .44")
