FROM continuumio/anaconda3

RUN pip install --upgrade pip

RUN apt update
RUN apt install -y libglu1-mesa-dev 

RUN conda install jupyter -y --quiet
RUN mkdir -p /opt/notebooks

ENTRYPOINT [ "/bin/bash", "-c", "jupyter notebook --notebook-dir=/opt/notebooks --ip='*' --port=8888 --no-browser --allow-root" ]
