#!/bin/bash
rm -f /home/output/*

nnUNet_predict -i /home/input -o /home/output --task_name "Task006_Lung" -m  3d_fullres
