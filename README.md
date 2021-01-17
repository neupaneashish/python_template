# Overview
This is a template repo for Machine Learning projects in python using Github for code management, and Azure Machine Learning for model management. 

# Before using for a project
Change project name in the following locations:
- .github/workflows/ci.yml
- test/unit/test_dummy.py
- environment.yml
- tox.ini
- setup.py
And check LICENSE

# Directory Structure (including untracked files)
![Dir Structure](docs/image.jpg?raw=true)

Untracked files/folders on root level:
|- data : data stored here
|- models: models here

# Dataset
In directory data

# Model
In directory models

# Setup
Initial setup. Repository and environment etc.
- install python 3.7
- install conda 
- git clone this repo

## Data Science
Setting up to explore the dataset, engineer features, and evaluate models.
- set up jupyter notebook environment
- install relevant packages

## Engineering
Setting up to make the selected models from previous step usable- 
- TODO: conda env setup (VS Code optional)
- TODO: env variables (secrets)
- TODO: Local Unit tests, and local deployment testing 
- TODO: Integration pipeline with linting and unit tests
- TODO: AzureML resource creation
- TODO: AzureML real-time endpoint deployment
- TODO: Deployed model E2E test
- TODO: Training Pipeline
- TODO: Test training pipeline
- TODO: How to deal with Data Drift?
- TODO: Implement a second model, and use an ensemble of classifiers for classification
 