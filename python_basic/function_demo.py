"""
作用1,容易复用
作用2,容易阅读
作用3,容易测试
"""


def hello(name: str = "some body", age: int = 18):
    """
    函数的描述
    :param name: 参数name的描述
    :param age: 参数age的描述
    :return:
    """
    print("hello %s,your age is %s" % (name, age))
    return "return some value"


hello()
hello("路飞")
hello(age=90)

result = hello("香吉士", 18)
print(result)

# 元组参数,可传入任意数量的字符串
def hello_every_one(message, *names):
    for name in names:
        print(name)
    print(message)


hello_every_one("你好", "香吉士", "路飞", "娜美")


# 字典参数
def print_every_one(**person_dic):
    print(person_dic)
    for key, value in person_dic.items():
        print("%s 是 %s 的" % (key, value))


print_every_one(香吉士="男", 路飞="男", 娜美="女")  # 只是演示,请大家不要用中文变量名
