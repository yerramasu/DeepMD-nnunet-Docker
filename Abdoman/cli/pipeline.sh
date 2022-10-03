#!/bin/bash
ls /home/nnUNet/input
rm /home/output/*
cd /home
# nohup python App.py &
rm /home/output/*
nnUNet_predict -i /home/input -o /home/output --task_name "Task017_AbdominalOrganSegmentation" -m  3d_fullres
