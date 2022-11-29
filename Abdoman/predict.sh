#!/bin/bash
# rm -f /home/output/*
# rm /home/output/*
# nnUNet_predict -i /home/input -o /home/output --task_name "Task017_AbdominalOrganSegmentation" --model 2d --disable_tta
nnUNet_predict -i $inputDir -o $outDir --task_name "Task017_AbdominalOrganSegmentation" --model 2d --disable_tta
# cp -r $inputDir/* /home/input &&
# cp -r $outDir/* /home/output &&
# rm -rf $inputDir &&
# rm -rf $outDir
