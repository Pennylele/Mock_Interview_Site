import os, jpype

jarpath = os.path.join(os.path.abspath('.'), 'test.jar')
jpype.startJVM(jpype.getDefaultJVMPath(), "-ea", "-Djava.class.path=%s" % jarpath)
Test = jpype.JClass('com.Test')
t = Test()
res = t.run("hello world")
print(res)
jpype.shutdownJVM()
