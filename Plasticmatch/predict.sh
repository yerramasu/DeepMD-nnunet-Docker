#!/bin/bash
# rm -f /home/output/*
echo $(plastimatch --version) &&
segimage2itkimage --help &&
echo $(svn --version | head -n 2) &&
cd /home/output &&

# nnUNet_predict -i /home/input -o /home/output --task_name "Task017_AbdominalOrganSegmentation" -m  3d_fullres
plastimatch convert --input /home/input --output-img outfile_0001.nii.gz 