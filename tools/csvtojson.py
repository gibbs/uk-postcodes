#!/usr/bin/env python
#
# Convert postcode.csv to JSON
#
import os, csv, json

# Paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = SCRIPT_DIR + '/../'
DATA_DIR = SCRIPT_DIR + '/../data/'

# Postcode files
csv_file = open(ROOT_DIR + 'postcodes.csv', 'r')
json_file = open(DATA_DIR + 'postcodes.json', 'w')

# Read CSV and get headers
reader = csv.DictReader(csv_file)
rows = list(reader)

# JSON start
json_file.write('[')

for x, row in enumerate(rows):
    json.dump(row, json_file, indent=2)

    if x != (len(rows) -1):
        json_file.write(',')

# JSON end
json_file.write(']')
