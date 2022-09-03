#!/bin/bash
ls /home/nnUNet/input
cd /home
python App.py
# nnUNet_predict -i /home/input -o /home/output --task_name "Task017_AbdominalOrganSegmentation" -m  3d_fullres
