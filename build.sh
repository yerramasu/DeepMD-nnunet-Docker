docker build --no-cache -t anilyerramasu/nnunet-spleen_gpu .
After building the image using docker build command,  the container using the following:
docker build --no-cache -t anilyerramasu/plasticmatch .
docker run   --rm -p 9000:5000 -v $(pwd)/input:/home/input -v $(pwd)/output:/home/output anilyerramasu/plasticmatch 

Run Command
docker build --no-cache -t anilyerramasu/segabdominalorgan_3d_gpu .
docker run --gpus all   -d --ipc=host --rm -p 5000:5000 -v $(pwd)/input:/home/input -v $(pwd)/output:/home/output  anilyerramasu/segabdominalorgan_3d_gpu 
docker run --gpus all    --ipc=host --rm -p 5000:5000 -v $(pwd)/input:/home/input -v $(pwd)/output:/home/output  anilyerramasu/segabdominalorgan_3d_gpu 

docker build --no-cache -t anilyerramasu/segpancreas_3d_gpu .


docker run --gpus all --ipc=host --rm -p 5000:5000 -v $(pwd)/input:/home/input -v $(pwd)/output:/home/output anilyerramasu/seghepaticvessel_3d_gpu


docker run --gpus all   -d --ipc=host --rm -p 5000:5000 -v $(pwd)/input:/home/input -v $(pwd)/output:/home/output  anilyerramasu/imageupload
anilyerramasu/seglung_3d_gpu_cli

kubectl -n argo exec -it <podname> -- /bin/sh
kubectl -n argo exec -it uploader-deployment-74798f5554-nmg9r -- /bin/sh