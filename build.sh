docker build -t anilyerramasu/nnunet .
After building the image using docker build command,  the container using the following:

Run Command

docker run --rm --gpus all  --name=anilyerramasu/nnunet-spleen -v /home/ubuntu/DeepMD-nnunet-Docker/input:/home/nnUNet/input -v /home/ubuntu/DeepMD-nnunet-Docker/output:/home/nnUNet/output
