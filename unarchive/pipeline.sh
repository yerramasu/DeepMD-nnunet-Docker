#!/bin/bash
cd /home/input &&
rm -rf /home/output/temp
rm -f /home/output/*
ls /home/output
# rm -rf /home/output/temp
tar xf *.tar  -C /home/output --strip-components 1
ls /home/output | wc -l