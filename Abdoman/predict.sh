#!/bin/bash
rm -f /home/output/*

nnUNet_predict -i /home/input -o /home/output --task_name "Task017_AbdominalOrganSegmentation" -m  3d_fullres