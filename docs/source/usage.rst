## Global Lightcast Smart Dataset Client

The goal of this project is to propose a Python Client, easy to use, ready for everyone to access and use in few seconds the Global Lightcast Smart Dataset

The client covers different needs and question:
- UK Occupation Insights (contents, trends and projection by occupation and area in UK)
- Global Occupation Insights (contents, trends and projection by occupation and area, globallu)


### Install

To install or install/upgrade the package it's best to use pip:
`pip install -U lightcast-smart-dataset`

### How it works

You can use the client in two ways:
- Command line
- Python code

This module is using [docopt](http://docopt.org/) to parse command line arguments.

It proposes different methods:

1. Get the occupation insights for an occupation in a area of UK
  * `lightcast-smart-dataset uk occupation-insight soc --username=**** --password=**** --occupation="Programmers and software development professionals" --area="Camden and City of London"`
  * `lightcast-smart-dataset uk occupation-insight occupation --username=***** --password=**** --occupation="Programmers and software development professionals" --area="Camden and City of London"`
2. Get the occupation insights for software developers in Milan, Italy
  * `lightcast-smart-dataset global occupation-insight occupation --username=***** --password=**** --occupation="Business Development / Sales Manager" --area="Milan (ITA)"  --occupation-level=3 --area-level=2`
3. Get a taxonomy
     * `lightcast-smart-dataset taxonomy soc4 --username=**** --password=****`

### Results

The command line interface will create different Excel file with different sheets:
- the current 12 months of unique job postings vs the last 12 months of unique job postings
- the top 10 common skills, top 10 specialized skills in the area refered to the last 12 months for the requested occupation
- the top 10 job tiles in the area refered to the last 12 months for the requested occupation
- the top 10 employers in the area refered to the last 12 months for the requested occupation (only employers, no staffic company)
