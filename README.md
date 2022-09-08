# DeepMD-nnunet-Docker

Install microk8s


microk8s helm3 repo remove nvidia

sudo snap remove microk8s
sudo snap install microk8s --classic --channel=1.22
sudo usermod -a -G microk8s $USER
sudo chown -f -R $USER ~/.kube
#su - $USER
newgrp microk8s

microk8s status --wait-ready
microk8s kubectl get nodes
microk8s kubectl get services

microk8s enable gpu