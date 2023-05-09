# Integrated NILM toolkit and SDK for Docker
This is a data science Non-Intrusive Load Monitoring development docker with Python.  

What is about this Docker?
NILM is a foundational algorithm that can disaggregate a home's power usage into the individual appliances that are running, identify energy conservation opportunities. This integrated development NILM docker provides the use and evaluation of below toolkits:
- [nilmtk](https://github.com/nilmtk/nilmtk)
- [nilmtk-contrib](https://github.com/nilmtk/nilmtk-contrib) 
- [neuralnilm by Joseluis](https://github.com/joseluis1061/neuralnilm.git)
Others:
- [neuralnilm by Jack Kelly](https://github.com/JackKelly/neuralnilm)

This docker can examine and evaluate the anatomy of NILM, looking at techniques using load monitoring, event detection, feature extraction, classification, and accuracy measurement.

# Getting Started
There are a couple of things needed for the script to work.

## Prerequisities
Docker, either the Community Edition (CE) or Enterprise Edition (EE), needs to be installed on your local computer.  Docker installation instructions can be found [here](https://docs.docker.com/install/).  

## Build Image
To start building the image - and have a shell - use the following command (the container will be deleted after exiting the shell):
```
docker build -f Dockerfile -t dasc-miniana3-nilmtk:V2.3 .
```

## Run Image
To start the container "dasc-miniana3-nilmtk:V2.3", see below
```
docker run -tid --name mynilm \
  -e "TZ=Asia/Kuala_Lumpur" -p 8118:8881 \
  -v /home/work:/home/work dasc-miniana3-nilmtk:V2.3
```

## Versioning
This project uses [SemVer](http://semver.org/) for versioning. 

## Authors
- KK Yong
