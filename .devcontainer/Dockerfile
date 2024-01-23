FROM python:latest

RUN apt update && apt upgrade -y

RUN pip install --upgrade pip

RUN pip install ipykernel -U --user --force-reinstall

# https://matplotlib.org/ipympl/
RUN pip install ipympl 
