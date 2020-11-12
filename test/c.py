#!/usr/bin/env python
# test_subprocess.py
import os
import subprocess

subprocess.call([os.getcwd() + '/a.out', '99'])
