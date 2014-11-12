#!/usr/bin/env python
import subprocess
import argparse,os
from os.path import expanduser

source_directory = os.path.dirname(os.path.realpath(__file__))
working_directory = os.getcwd()
home_directory = expanduser("~")

def script(cmd):
    print cmd
    subprocess.call(cmd, shell=True)

if __name__  == "__main__":
	script("uwsgi --http :8001 --wsgi-file test.py")
