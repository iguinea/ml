.PHONY: run


# https://jupyter-docker-stacks.readthedocs.io/en/latest/

# GPU
# https://github.com/iot-salzburg/gpu-jupyter


notebook_run: 
	@docker run -it --name lfd273 --rm -p 10000:8888 -v "${PWD}":/home/jovyan/work quay.io/jupyter/datascience-notebook:2023-11-17

notebook_gettoken:
	@docker exec -it lfd273 jupyter notebook list | cut -d\= -f2|cut -d \  -f1 |tail -1

notebook_bash:
	@docker exec -it lfd273 bash


notebook_gpu_run: 
	@docker run -it --name lfd273 --rm -p 10000:8888 -v "${PWD}":/home/jovyan/work --gpus all nvidia/cuda:12.0.1-cudnn8-runtime-ubuntu22.04 nvidia-smi


# SEGUIR ESTE EJEMPLO
#https://www.mrdbourke.com/pytorch-apple-silicon/

conda_install:
	brew install --cask anaconda
	wget "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-arm64.sh?ref=mrdbourke.com" -O ~/Downloads/Miniforge3-MacOSX-arm64.sh
	chmod +x ~/Downloads/Miniforge3-MacOSX-arm64.sh
	sh ~/Downloads/Miniforge3-MacOSX-arm64.sh
	source ~/miniforge3/bin/activate
	pip3 install torch torchvision torchaudio

conda_create:
	conda create --prefix ./env python=3.8

conda_activate:
	conda activate ././env
	jupyter notebook
#
# To activate this environment, use
#
#     $ conda activate /Users/iguinea/Personal/LFD273/env
#
# To deactivate an active environment, use
#
#     $ conda deactivate
