import os
import sys

input=sys.argv[1]
print("Input ", input)

for i in range(2, len(sys.argv)):
    label=sys.argv[i]
    name=input.split('.', 1)[0] + "_" + label
    ext="." + input.split('.', 1)[1]
    ext2 = ".nii"
    cmd1="c3d " + input + " -thresh " + label+ " " + label +" 1 -1 -smooth 0.8vox -o " + name + ext
    cmd2="vtklevelset " + name + ext + " " + name + ".vtk 0.0"
    cmd3="rm " + name + ext
    #print(cmd1)
    os.system(cmd1)
    #print(cmd2)
    os.system(cmd2)
    #print(cmd3)
    os.system(cmd3)
