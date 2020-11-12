import os.path, subprocess
from subprocess import STDOUT, PIPE


def compile_java(java_file):
    subprocess.check_call(['javac', java_file])


def execute_java(java_file):
    cmd = ['java', java_file]
    proc = subprocess.Popen(cmd, stdout=PIPE, stderr=STDOUT)
    input = subprocess.Popen(cmd, stdin=PIPE)
    print(proc.stdout.read())


compile_java("Temp.java")
execute_java("Temp")
