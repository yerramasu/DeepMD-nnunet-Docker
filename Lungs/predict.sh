#!/bin/bash
# rm -f /home/output/*

# nnUNet_predict -i /home/input -o /home/output --task_name "Task006_Lung" -m  3d_fullres
nnUNet_predict -i $inputDir -o $outDir --task_name "Task006_Lung" --model 2d --disable_tta
# cp -r $inputDir/* /home/input &&
