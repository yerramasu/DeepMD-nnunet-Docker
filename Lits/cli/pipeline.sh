#!/bin/bash
ls /home/nnUNet/input
cd /home
# nohup python App.py &
nnUNet_predict -i /home/input -o /home/output --task_name "Task003_Liver" -m  3d_fullres


