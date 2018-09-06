"""
1. 防止程序崩溃
2.

"""

if __name__ == '__main__':

    # 异常演示1
    print(5 / 0)

    try:
        print(5 / 0)
    except ZeroDivisionError:
        print("0不能作为除数")

    # 异常演示2
    file_path = '/Users/lichao/Documents/Code/bus-service/bus-starters/pom.xml'
    false_file_path = "a.txt"
    with open(false_file_path) as txt_file:
        for line in txt_file:
            print(line)

    try:
        file_path = '/Users/lichao/Documents/Code/bus-service/bus-starters/pom.xml'
        false_file_path = "a.txt"
        with open(false_file_path) as txt_file:
            for line in txt_file:
                print(line)
    except FileNotFoundError:
        print("文件不存在")


    # 抛出异常

    class NotHumanAge(Exception):
        pass


    def check_age(age):
        if age < 0 or age > 150:
            raise NotHumanAge


    check_age(-1)
    check_age(180)


# 定义异常
class NetworkError(Exception):
    pass


class HostnameError(NetworkError):
    pass


class TimeoutError(NetworkError):
    pass


class ProtocolError(NetworkError):
    pass


# 常见的异常
"""
AssertionError	assert（断言）语句失败
AttributeError	试图访问一个对象没有的属性，比如foo.x ，但是foo没有x这个属性。
IOError	输入/输出异常，基本上是无法打开文件。
ImportError	无法引入模块或者包，基本上是路径问题
IndentationError	语法错误，代码没有正确对齐
IndexError	下标索引超出序列边界，比如当x只有三个元素，却试图访问x[5]
KeyError	试图访问字典里不存在的键
KerboardInterrupt	Ctrl + C 被按下
NameError	使用一个还未被赋值予对象的变量
SyntaxError	Python代码非法，代码不能解释
TypeError	传入对象类型与要求的不符
UnboundLocalError	试图访问一个还未被设置的局部变量，基本上是由于另一个同名的全局变量，导致你以为正在访问它
ValueError	传入一个调用者不期望的值，即使值的类型是正确的
"""
