#!/bin/sh
conda env create -f environment.yaml
conda activate $my_env_name
pip install -e .
pre-commit install
