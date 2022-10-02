#!/bin/bash
ls /home/nnUNet/input
cd /home
# nohup python App.py &
rm /home/output/*
nnUNet_predict -i /home/input -o /home/output --task_name "Task006_Lung" -m  3d_fullres
