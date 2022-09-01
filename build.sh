docker build --no-cache -t anilyerramasu/nnunet-spleen_gpu .
After building the image using docker build command,  the container using the following:

Run Command
docker run  --gpus all -it --rm -v $(pwd)/input:/home/input -v $(pwd)/output:/home/output  anilyerramasu/nnunet-spleen_gpu1
