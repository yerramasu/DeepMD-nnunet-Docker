docker build -t anilyerramasu/nnunet:beta .
After building the image using docker build command,  the container using the following:

Run Command
docker run anilyerramasu/nnunet-spleen:beta --gpus all --rm -v /home/ubuntu/DeepMD-nnunet-Docker/input:/home/in -v /home/ubuntu/DeepMD-nnunet-Docker/output:/home/out