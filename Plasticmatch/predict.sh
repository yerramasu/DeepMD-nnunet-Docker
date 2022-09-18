#!/bin/bash
# rm -f /home/output/*
echo $(plastimatch --version) &&

cd /home/output &&

# nnUNet_predict -i /home/input -o /home/output --task_name "Task017_AbdominalOrganSegmentation" -m  3d_fullres
plastimatch convert --input /home/input --output-img outfile_0000.nii.gz 
