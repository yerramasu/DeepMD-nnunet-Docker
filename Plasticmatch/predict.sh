#!/bin/bash
rm -f /home/output/*
echo $(plastimatch --version)
segimage2itkimage --help
echo $(svn --version | head -n 2)
# nnUNet_predict -i /home/input -o /home/output --task_name "Task017_AbdominalOrganSegmentation" -m  3d_fullres
