#!/bin/bash
# rm -f /home/output/*

nnUNet_predict -i $inputDir -o $outDir --task_name "Task017_AbdominalOrganSegmentation" -m  3d_fullres &&
cp -r $inputDir/* /home/input &&
cp -r $outDir/* /home/output &&
rm -rf $inputDir &&
rm -rf $outDir
