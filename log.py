#!/usr/bin/env python3

import sys

class colors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def info(s):
	print(s)

def success(s):
	print(f"{colors.OKGREEN}{s}{colors.ENDC}")

def warning(s):
	print(f"{colors.WARNING}{s}{colors.ENDC}")

def error(s):
	print(f"{colors.FAIL}{s}{colors.ENDC}")

def crit(s):
	raise Exception(s)
