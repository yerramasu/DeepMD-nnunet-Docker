#!/bin/bash
ls /home/nnUNet/input
rm /home/output/*
cd /home
nnUNet_predict -i /home/input -o /home/output --task_name "Task007_Pancreas" -m  3d_fullres
