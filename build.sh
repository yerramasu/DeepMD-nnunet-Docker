docker build -t anilyerramasu/nnunet-spleen_gpu .
After building the image using docker build command,  the container using the following:

Run Command
docker run --gpus all   -d --ipc=host --rm -p 5000:5000 -v $(pwd)/input:/home/input -v $(pwd)/output:/home/output  anilyerramasu/segabdominalorgan_3d_gpu 




