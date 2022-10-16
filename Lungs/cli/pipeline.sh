#!/bin/bash
ls /home/nnUNet/input
cd /home
# nohup python App.py &
rm /home/output/*
nnUNet_predict -i /home/input -o /home/output --task_name "Task006_Lung" --model 2d --disable_tta 
