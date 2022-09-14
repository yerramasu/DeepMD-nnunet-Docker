#!/bin/bash
ls /home/nnUNet/input
cd /home
nnUNet_predict -i /home/input -o /home/output --task_name "Task055_SegTHOR" -m  3d_fullres
