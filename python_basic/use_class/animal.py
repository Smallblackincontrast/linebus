"""
    描述类的作用
"""


class Animal:
    type = "animal"

    def __init__(self, height: float, weight: float, age: int):
        """

        :param height: 身高,单位为米
        :param weight: 体重,单位为公斤
        :param age: 年龄,单位为岁
        """
        self.height = height
        self.weight = weight
        self.age = age

    def breathe(self):
        print("呼吸....")

    # 一些不常用的魔术方法
    """
    魔术方法	调用方式	解释
    __new__(cls [,...])	instance = MyClass(arg1, arg2)	__new__ 在创建实例的时候被调用
    __init__(self [,...])	instance = MyClass(arg1, arg2)	__init__ 在创建实例的时候被调用
    __cmp__(self, other)	self == other, self > other, 等。	在比较的时候调用
    __pos__(self)	+self	一元加运算符
    __neg__(self)	-self	一元减运算符
    __invert__(self)	~self	取反运算符
    __index__(self)	x[self]	对象被作为索引使用的时候
    __nonzero__(self)	bool(self)	对象的布尔值
    __getattr__(self, name)	self.name # name 不存在	访问一个不存在的属性时
    __setattr__(self, name, val)	self.name = val	对一个属性赋值时
    __delattr__(self, name)	del self.name	删除一个属性时
    __getattribute(self, name)	self.name	访问任何属性时
    __getitem__(self, key)	self[key]	使用索引访问元素时
    __setitem__(self, key, val)	self[key] = val	对某个索引值赋值时
    __delitem__(self, key)	del self[key]	删除某个索引值时
    __iter__(self)	for x in self	迭代时
    __contains__(self, value)	value in self, value not in self	使用 in 操作测试关系时
    __concat__(self, value)	self + other	连接两个对象时
    __call__(self [,...])	self(args)	“调用”对象时
    __enter__(self)	with self as x:	with 语句环境管理
    __exit__(self, exc, val, trace)	with self as x:	with 语句环境管理
    __getstate__(self)	pickle.dump(pkl_file, self)	序列化
    __setstate__(self)	data = pickle.load(pkl_file)	序列化
    """
