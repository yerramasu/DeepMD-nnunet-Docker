#!/bin/bash
ls /home/nnUNet/input
nnUNet_predict -i /home/in -o /home/out --task_name "Task055_SegTHOR" -m 3d_fullres
