from pathlib import Path
from argparse import ArgumentParser
from sys import exit
from measurement.sampling_process import prepare_sampling

try:
    _parser = ArgumentParser(description='DBMake')
    _parser.add_argument('-f', '--file', dest='file', default=0)
    args = _parser.parse_args()
    prepare_sampling(args.file)
except Exception as e:
    exit(1)