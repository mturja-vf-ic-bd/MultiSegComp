#!/usr/bin/env bash

gt_dir=/home/turja/MultiSegComp/input/testing-labels
test_dir=/home/turja/MultiSegComp/input/Martin

for file in `ls $gt_dir | grep nii.gz`; do
    a=`echo $file | cut -d '_' -f 1`
    b=`echo $file | cut -d '_' -f 2`
    sub=${a}_${b}
    echo "Processing : $sub"

    groundtruth=${gt_dir}/${sub}_glm.nii.gz
    infile=${test_dir}/${sub}_seg_subcortical.nii.gz

    if [ ! -f ${infile} ]; then
        infile=${test_dir}/${sub}_seg_subcortical.nrrd
    fi

    if [ -f ${infile} ]; then

        basename=`echo ${infile} | cut -d '.' -f 1`
        basenamegt=`echo ${groundtruth} | cut -d '.' -f 1`
        ext=`echo ${infile} | cut -d '.' -f 2`
        if [ "${ext}" = "nrrd" ]; then
            echo "Got ext = ${ext}"
            python nrrdToNifti.py $infile
            infile2=${basename}.nii.gz
        else
            infile2=$infile
        fi

        #labels="1 2 3 4 5 6 7 8 9 10 11 12 13 14"
        labels="23 30 31 32 36 37 47 48 51 52 55 56 57 58 59 60"
        #labels="47 46"
        #python createSurf.py $infile2 $labels #create iso surface
        #python createSurf.py $groundtruth $labels #same for ground truth

        # move center of mass
        IFS=' ' # space is set as delimiter
        read -ra LBL <<< "$labels" # str is read into an array as tokens separated by IFS
        for label in ${LBL[@]}; do
            python findCOM.py ${basename}_${label}.vtk ${basename}_${label}.ply
            python findCOM.py ${basenamegt}_${label}.vtk ${basenamegt}_${label}.ply
            #disLine=`MeshValmet -absolute -in1 ${basenamegt}_${label}.iv -in2 ${basename}_${label}.iv | tail -15 | grep 'Max'` # get the hd distance
            #echo "${label} ${disLine}" >> ${gt_dir}/hd/${sub}_hausdorff_out.txt # write hausdorff distance to a file
        done
    fi
done

python calculateAvgHd.py ${gt_dir}/hd > "AvgHdDistance.txt" #Calculate average hd distance