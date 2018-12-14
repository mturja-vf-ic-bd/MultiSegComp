#!/bin/bash

input=$1
label=$2
name=`echo $input | cut -d '.' -f 1`
c3d $input -thresh $label $label 1 -1 -smooth 0.8vox -o ${name}_${label}.nii
vtklevelset ${name}_${label}.nii ${name}_${label}.vtk 0.0
rm ${name}_${label}.nii

