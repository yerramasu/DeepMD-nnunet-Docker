#!/bin/bash
# rm -f /home/output/*

nnUNet_predict -i $inputDir -o $outDir --task_name "Task003_Liver" --model 2d --disable_tta
