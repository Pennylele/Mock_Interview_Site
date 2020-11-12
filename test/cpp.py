import sys
from subprocess import *
import subprocess

#
# path = r'/Users/ligangye/PycharmProjects/django/mock_interview/test/hello.cpp'  # r表示忽略转译字符
# string_para = 'h'
# int_para = '10'
# p = Popen(path, stdin=PIPE, stdout=PIPE, encoding='gbk')
# result = p.communicate(input=string_para)
# print(result[0])


#
# file_output = open("debug.txt", "w")
# subprocess.Popen("ipconfig", stdout=file_output).wait()
# file_output.close()
#
# cmd_sys = subprocess.Popen('ipconfig', stdout=subprocess.PIPE)
# cmd_res = cmd_sys.stdout.read()


s1 = subprocess.check_output(
    "g++ /Users/ligangye/PycharmProjects/django/mock_interview/test/hello.cpp `pkg-config --cflags --libs opencv` -lm  -o out2;./out2",
    shell=True)
print("TYPE ==> ", type(s1), " size : ", sys.getsizeof(s1))
print(s1.decode("utf-8"))
