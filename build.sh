After building the image using docker build command,  the container using the following:

Run Command
docker run --gpus "device=1" --ipc=host --name=deepmd_nnUNet -it --rm -v /vault/aberg_vault:/workspace/nnUNet deepmd-nnunet:v3.0-12.31.2020-1