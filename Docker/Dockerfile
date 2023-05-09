##
# Description   : This is to build an integrated nilm-cnn development environment based on nilmtk, 
#                 nilm-contrib and neuralnilm packages, which based on Anaconda3 2011.11 release.
#                 It setup the auto load jupyter notebook
#
# Docker Cmmd   : docker build -f Dockerfile -t dasc-miniana3-nilmtk:V2.2 .
#               : docker run -tid --name mynilm -e "TZ=Asia/Kuala_Lumpur" -p 8118:8881 -v /home/work:/home/work dasc-miniana3-nilmtk:V1.0
#
# Version       : 2.2
#
# Created Date  : 9/4/2022
# Modified Date : 5/8/2022
#
# Updates:
# --------
# - Install g++ (required for theano) and vim 
# - Create manual setup for neuralnilm package installation
#
##

FROM continuumio/miniconda3

# Make RUN commands use `bash --login`:
#
SHELL ["/bin/bash", "--login", "-c"]

# Perform apt install for g++ (required for theano optimization)
#
RUN apt update && apt install -y g++ && rm -rf /var/lib/apt/lists/*
RUN apt update && apt install -y vim && rm -rf /var/lib/apt/lists/*

RUN mkdir -pv /etc/ipython/
COPY config/ipython_config.py /etc/ipython/ipython_config.py

# Create the conda environment: nilmtk-env
# 
COPY environment.yml .
RUN conda env create -f environment.yml

# Initialize conda in bash config fiiles:
#
RUN conda init bash

# Activate the environment, and make sure it is in "nilmtk-env", but not "base"
#
RUN echo "conda init bash" > ~/.bashrc
RUN echo "conda activate nilmtk-env" >> ~/.bashrc
SHELL ["/bin/bash", "--login", "-c"]

# Run PIP install the required package for nilm-cnn, the source is 
# from https://github.com/joseluis1061/neuralnilm
#
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Install neralnilm package from https://github.com/joseluis1061/neuralnilm.git
# 
COPY neuralnilm.tgz .
RUN tar xzvf neuralnilm.tgz
WORKDIR /neuralnilm
RUN python setup.py install

# Install Jupyter notebook
#
WORKDIR /
RUN conda install -c conda-forge notebook
RUN conda install -c conda-forge nb_conda_kernels
RUN conda install -c conda-forge jupyter_contrib_nbextensions

# Install jupyter extensions
#
RUN jupyter contrib nbextension install

# Enable jupyter extensions
#
RUN jupyter nbextensions_configurator enable
RUN jupyter nbextension enable collapsible_headings/main
RUN jupyter nbextension enable rubberband/main
RUN jupyter nbextension enable toc2/main
RUN jupyter nbextension enable codefolding/main
RUN jupyter nbextension enable scratchpad/main

# Create Working Directory
#
RUN mkdir -p /home/work

# Change path
#
WORKDIR /home/work

# Create port for Jupyter notebook
#
EXPOSE 8881

# Copy entryping script
#
COPY entrypoint.sh /

# Final
#
#ENTRYPOINT ["jupyter", "notebook", "--no-browser", "--ip=0.0.0.0", "--port=8881", "--NotebookApp.token=''", "--allow-root", "--NotebookApp.password=''", "--NotebookApp.notebook_dir='/home/work'"]
ENTRYPOINT ["/bin/bash", "-c", "/entrypoint.sh"]
