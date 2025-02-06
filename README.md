# Spacewalks

## Overview
Spacewalks is a Python analysis tool for researchers to generate visualisations
and statistical summaries of NASA's extravehicular activity datasets.

## Features
Key features of Spacewalks:

- Generates a CSV table of summary statistics of extravehicular activity crew sizes
- Generates a line plot to show the cumulative duration of space walks over time

## Pre-requisites

Spacewalks was developed using Python version 3.12

To install and run Spacewalks you will need have Python >=3.12 
installed. You will also need the following libraries (minimum versions in brackets)

- [NumPy](https://www.numpy.org/) >=2.0.0 - Spacewalk's test suite uses NumPy's statistical functions
- [Matplotlib](https://matplotlib.org/stable/index.html) >=3.0.0  - Spacewalks uses Matplotlib to make plots
- [pytest](https://docs.pytest.org/en/8.2.x/#) >=8.2.0  - Spacewalks uses pytest for testing
- [pandas](https://pandas.pydata.org/) >= 2.2.0 - Spacewalks uses pandas for data frame manipulation

## Installation instructions

```bash
git clone https://github.com/koriege/spacewalks
cd spacewalks
```
optional:
```bash
python3 -m venv /path/to/venv_dir 
source /path/to/venv_dir/bin/activate
```
pip install -r requirements.txt
python eva_data_analysis.py
```

## Usage example

```bash
cd spacewalks
```
optional:
```bash
source /path/to/venv_dir/bin/activate
```
```bash
python eva_data_analysis.py [/path/to/input_json] [/path/to/ouput_csv]
```
png of cumulative hours in space will be created in `spacewalks/results` directory