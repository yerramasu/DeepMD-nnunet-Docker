#!/bin/bash
rm -f /home/output/*
# echo $(plastimatch --version) &&
# rm  /home/output/*
# pip3 install dicom2nifti
cd /home/output 
ls -al /home/input | wc
# cd /home
# python3 dcm2nifty.py
# cd output
# mv *.nii.gz outfile_0000.nii.gz
# nnUNet_predict -i /home/input -o /home/output --task_name "Task017_AbdominalOrganSegmentation" -m  3d_fullres
plastimatch convert --input /home/input --output-img outfile_0000.nii.gz 
