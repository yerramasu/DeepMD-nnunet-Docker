#!/bin/bash
rm -f /home/output/* &&
cd /home &&
python3 process_image.py >> out.txt
nnUNet_predict -i /home/input -o /home/output --task_name "Task006_Lung" -m  3d_fullres
