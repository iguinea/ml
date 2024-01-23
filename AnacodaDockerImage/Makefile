PHONY: help

help:
	@echo "make https://hub.docker.com/r/continuumio/anaconda3"


build:
	docker build -t anaconda:local .
#	docker run -i -t -p 8888:8888 continuumio/anaconda3 /bin/bash -c "\
    	conda install jupyter -y --quiet && \
    	mkdir -p /opt/notebooks && \
    	jupyter notebook \
    	--notebook-dir=/opt/notebooks --ip='*' --port=8888 \
    	--no-browser --allow-root"
	
launch:
	docker run -it --rm --name anaconda -p 8888:8888 anaconda:local 

dw_custom: 
	wget https://repo.anaconda.com/archive/Anaconda3-2023.09-0-Linux-aarch64.sh

build_custom:
	docker build -t anaconda:local . -f Dockerfile.custom
