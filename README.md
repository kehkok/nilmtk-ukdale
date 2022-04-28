# Exploration of nilmtk with ukdale in Docker

This material helps an apprentice to explore and deep-dive into NILTMTK with UKDALE dataset.    In order to ease up the installation, there is an custom setup NILMTK with Jupyter Notebook using docker.  It contains the required python packages, it provides the **Dockerfile** for building the docker image. However, this project is an unoffical abd not related to NILMTK.  

# Background
NILMTK is an open source toolkit for non-intrusive load monitoring.  It contains rich set of APIs for exploring energy disaggregation.  The information is well published in [NILMTK github](https://github.com/nilmtk/nilmtk).   

UK-Dale (UK Domestic Appliance-Level Electricity) is a dataset that records the power demand from five houses.   There is low sampling rate as every six seconds and also high sampling rate in 16kHz.  The detail can be found in [Jack Kelly](https://jack-kelly.com/data/) and [UKEDC](https://data.ukedc.rl.ac.uk/browse/edc/efficiency/residential/EnergyConsumption/Domestic).