# Tensorflow-GPU-Docker

Install Docker as per https://docs.docker.com/install/linux/docker-ce/ubuntu/

Install NVIDIA Drivers on your system

Install Nvidia-Docker as per  https://github.com/NVIDIA/nvidia-docker

docker build -t dl-docker:gpu -f Dockerfile.gpu .

nvidia-docker run -it -p 8888:8888 -p 6006:6006 -v /sharedfolder:/root/sharedfolder floydhub/dl-docker:gpu bash
