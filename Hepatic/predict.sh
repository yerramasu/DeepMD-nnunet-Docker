#!/bin/bash
rm -f /home/output/*

nnUNet_predict -i /home/input -o /home/output --task_name "Task008_HepaticVessel" --model 2d --disable_tta
