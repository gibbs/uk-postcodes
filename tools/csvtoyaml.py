#!/usr/bin/env python
#
# Convert postcode.csv to YAML
#
import os, csv, yaml

# Paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = SCRIPT_DIR + '/../'
DATA_DIR = SCRIPT_DIR + '/../data/'

# Postcode files
csv_file = open(ROOT_DIR + 'postcodes.csv', 'r')
yaml_file = open(DATA_DIR + 'postcodes.yaml', 'w')

# Read CSV and get headers
reader = csv.DictReader(csv_file)
rows = list(reader)

yaml.dump(rows, yaml_file, default_flow_style=False)
