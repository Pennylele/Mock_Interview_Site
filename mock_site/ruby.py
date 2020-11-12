import subprocess
from subprocess import STDOUT, PIPE

cmd = "ruby /Users/ligangye/PycharmProjects/django/mock_interview/staticfiles/temp.rb"
p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
output, errors = p.communicate()

print('start')
print(output)
print(errors)
print('end')
