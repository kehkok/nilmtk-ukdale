# Introduction

NILM (Non-Intrusive Load Monitoring) analytics is the process of using different types of analysis, such as signal processing, statistical analysis, and machine learning, deep learning and other methods, to figure out how different appliances in a building or home use energy.  The goal is to give people a detailed picture of how much energy each appliance uses and when it is being used. This knowledge can be used to find ways to save energy, make the best use of energy, and make energy use more efficient.  Furthermore, these analysis can also be used by utilities to keep track of and manage large-scale energy use and to better understand and control grid demand. By looking at how different households use energy, utilities can make targeted programmes to save energy and better handle the supply and demand of energy on the grid.

Thus, these materials are to assist an apprentice for exploring and deep-diving practically into NILM analytics.  Below open source systems are adopted:  

- NILMTK is an open source toolkit for non-intrusive load monitoring.  It contains rich set of APIs for exploring energy disaggregation.  The information is well published in [NILMTK github](https://github.com/nilmtk/nilmtk).
- [UK-Dale](https://data.ukedc.rl.ac.uk/browse/edc/efficiency/residential/EnergyConsumption/Domestic) dataset in h5 format. May refer to [UKEDC](https://data.ukedc.rl.ac.uk/browse/edc/efficiency/residential/EnergyConsumption/Domestic/UK-DALE-2017/UK-DALE-FULL-disaggregated)
- Python and Jupyter Notebook development environment either on Desktop or Docker.  The simple guideline to preparing a Docker is located at "Docker" folder with **Dockerfile** for building the docker image.

**Tutorial** folder consists of series of ipynb files to guide you through NILMTK.  It has three major modules:

1. Module 1 consists of Exploratory Data Analytics techniques with UK-DALE dataset.
2. Module 2 consists of NILMTK APIs for executing fundamental disaggregation algorithms Combinatorial Optimisation (CO), Factorial hidden markov models and Hart85.
3. Module 3 consists of advanced techniques to import custom dataset to NILMTK and executing fundamental disaggregation

This project is an unofficial  and also not related to core development of NILMTK. However, this is to prepare an easy guideline and setup for an apprentice to learn NILMTK instead.  

## Prerequisite

- NILMTK development environment either in Desktop or Docker
- [UK-Dale](https://data.ukedc.rl.ac.uk/browse/edc/efficiency/residential/EnergyConsumption/Domestic) (UK Domestic Appliance-Level Electricity) is a dataset that records the power demand from five houses.   There is low sampling rate as every six seconds and also high sampling rate in 16kHz.  The dataset in h5 format which requiring for the tutorial may refer to [UK-DALE h5](https://data.ukedc.rl.ac.uk/browse/edc/efficiency/residential/EnergyConsumption/Domestic/UK-DALE-2017/UK-DALE-FULL-disaggregated).  It need to place into "./Tutorial/Dataset" folder

## Discern an appliance load disaggregation problem

- **What?** To collect data about how much energy each device in a building or home uses. NILM analytics is the process of analysing this data to learn more about how each appliance uses energy.
- **Why?** Is important because it helps people understand how they use energy, find ways to save energy, and make the best use of energy. It can also be used by utilities to track and control how much energy is used on a big scale and to learn more about and control the demand on the grid.
- **Who?** Tracks and control how much energy is used by homeowners, building managers, and utilities.
- **When?** Uses all the time to track and analyse how energy is consumed. It can also be used on a regular basis to check how well energy-saving methods are working and find places where they could be better.
- **Where?** Uses in any building or home, also bigger scale by utilities to track and control how much energy is used in a certain area.
- **How?** Works by analysing the data that a NILM system makes by using methods like data visualisation, statistical analysis, and machine learning algorithms. In the power data, the goal is to find the unique energy signatures of each appliance and give a thorough breakdown of how much energy each appliance uses and when it is being used.

## Reference

- Jack & William published an informative journal, "The The UK-DALE dataset, domestic appliance-level electricity demand and whole-house demand from five UK homes" at 2015.  The details can be reached [here](https://www.nature.com/articles/sdata20157).
- [nilmtk package documentation 0.2](http://nilmtk.github.io/nilmtk/master/nilmtk.html)
- [Jack Kelly Data](https://jack-kelly.com/data/)
