import execjs


# from js_code import *


def js_from_file(file_name):
    """
    读取js文件
    :return:
    """
    with open(file_name, 'r', encoding='UTF-8') as file:
        result = file.read()

    return result


# 编译加载js字符串
context1 = execjs.compile(js_from_file('./norm.js'))

result1 = context1.call("add", 2, 3)

print(result1)
