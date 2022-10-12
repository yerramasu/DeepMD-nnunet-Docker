#!/bin/bash
ls /home/nnUNet/input
rm /home/output/*
cd /home
# nnUNet_predict -i /home/input -o /home/output --task_name "Task055_SegTHOR" -m  3d_fullres
nnUNet_predict -i /home/input -o /home/output --task_name "Task055_SegTHOR" --model 2d --disable_tta 
