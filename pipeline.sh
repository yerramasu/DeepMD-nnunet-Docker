#!/bin/bash
ls /home/nnUNet/input
nnUNet_predict -i /home/nnUNet/input -o /home/nnUNet/output --task_name "Task055_SegTHOR" -m 3d_fullres
