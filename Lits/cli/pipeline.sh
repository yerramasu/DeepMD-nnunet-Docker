#!/bin/bash
ls /home/nnUNet/input
cd /home
# nohup python App.py &
rm /home/output/*
# 2d --disable_tta 
# nnUNet_predict -i /home/input -o /home/output --task_name "Task003_Liver" -m  3d_fullres
nnUNet_predict -i /home/input -o /home/output --task_name "Task003_Liver" --model 2d --disable_tta 


