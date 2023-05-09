# Exploration of NILMTK algorithms

This material helps an apprentice to explore and understand the algorithms available in NILMTK namely, Hart85, Combinatorial Optimization(CO) and Factorial Hidden Markov Model(FHMM).    In order to ease up the installation, there is an custom setup NILMTK with Jupyter Notebook using docker.  It contains the required python packages, provides the **Dockerfile** for building the docker image. However, this project is an unoffical abd not related to NILMTK.  

# Background
NILMTK is an open source toolkit for non-intrusive load monitoring.  It contains rich set of APIs for exploring energy disaggregation.  The information is well published in [NILMTK github](https://github.com/nilmtk/nilmtk).
The source codes of the algorithms explored in this module are taken directly from the NILMTK API.   

UK-Dale (UK Domestic Appliance-Level Electricity) is a dataset that records the power demand from five houses.   There is low sampling rate as every six seconds and also high sampling rate in 16kHz.  The detail can be found in [Jack Kelly](https://jack-kelly.com/data/) and [UKEDC](https://data.ukedc.rl.ac.uk/browse/edc/efficiency/residential/EnergyConsumption/Domestic).

Jack & William published an informative journal, "The UK-DALE dataset, domestic appliance-level electricity demand and whole-house demand from five UK homes" at 2015.  The details can be reached [here](https://www.nature.com/articles/sdata20157).

# Reference
- [nilmtk package documentation 0.2](http://nilmtk.github.io/nilmtk/master/nilmtk.html)
- [NILMTK Contrib with API](https://github.com/nilmtk/nilmtk-contrib)
