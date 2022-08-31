docker build -t anilyerramasu/nnunet .
After building the image using docker build command,  the container using the following:

Run Command
docker run anilyerramasu/nnunet-spleen --gpus all --rm -v /home/ubuntu/DeepMD-nnunet-Docker/input:/home/nnUNet/input -v /home/ubuntu/DeepMD-nnunet-Docker/output:/home/nnUNet/output