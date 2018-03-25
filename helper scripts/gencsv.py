'''

usage: gencsv.py [-h] filename 

Generates CSV files for a given text file delimited by commas

positional arguments:
  filename             The text file which is to be converted to a CSV file

optional arguments:
  -h, --help     show this help message and exit

'''

import csv
import sys, os, argparse

parser = argparse.ArgumentParser(description='Generates CSV files for a given text file delimited by commas')
parser.add_argument('filename', metavar = 'filename', type = str, nargs = '?', help = 'Filename of comma seperated text file')

args = parser.parse_args()
csv_file = os.path.splitext(args.filename)[0] + ".csv"

in_txt = csv.reader(open(args.filename, "r"), delimiter = ',')
out_csv = csv.writer(open(csv_file, 'w'))
out_csv.writerows(in_txt)