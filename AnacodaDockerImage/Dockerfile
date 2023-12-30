FROM python:latest

RUN pip install --upgrade pip
ENTRYPOINT [ "/bin/bash" ]

WORKDIR /workdir
#ADD https://repo.anaconda.com/archive/Anaconda3-2023.09-0-Linux-aarch64.sh /tmp

COPY Anaconda3-2023.09-0-Linux-aarch64.sh /tmp

RUN chmod +x /tmp/Anaconda3-2023.09-0-Linux-aarch64.sh
RUN /tmp/Anaconda3-2023.09-0-Linux-aarch64.sh -b -p /opt/anaconda3
RUN rm /tmp/Anaconda3-2023.09-0-Linux-aarch64.sh


#Do you wish to update your shell profile to automatically initialize conda?
#This will activate conda on startup and change the command prompt when activated.
#If you'd prefer that conda's base environment not be activated on startup,
#   run the following command when conda is activated:
#
#conda config --set auto_activate_base false
RUN  /opt/anaconda3/condabin/conda config --set auto_activate_base false
#
#You can undo this by running `conda init --reverse $SHELL`? [yes|no]
#[no] >>> 
#
#You have chosen to not have conda modify your shell scripts at all.
#To activate conda's base environment in your current shell session:
#
#eval "$(/root/anaconda3/bin/conda shell.YOUR_SHELL_NAME hook)" 
RUN eval "$(/opt/anaconda3/condabin/conda shell.bash hook)" 
#
#To install conda's shell functions for easier access, first activate, then:
#
#conda init
#
#Thank you for installing Anaconda3!


RUN /opt/anaconda3/condabin/conda install anaconda-navigator -y
RUN /opt/anaconda3/bin/activate root
#ENTRYPOINT [ "/opt/anaconda3/bin/navigator" ]



apt install libglu1-mesa-dev


