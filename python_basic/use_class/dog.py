"""

"""
from python_basic.use_class.animal import Animal


class Dog(Animal):

    def __init__(self, height, weight, age, name):
        super().__init__(height, weight, age)
        self.name = name
        self.type = "dog"

    # classmethod 标记函数是另一种构造对方的方式
    @classmethod
    def buy(cls):
        return cls(50, 0.3, 10, "旺财")

    def say(self):
        print("汪 汪 汪...")

    # static method 标记函数不属于类的实例,只是放在类里面
    @staticmethod
    def compute_bmi(weight, height):
        # 体质指数（BMI）=体重（kg）÷身高^2（m）,当BMI指数为18.5～23.9时属正常
        bmi = weight / (height ** 2)
        if bmi > 23.9:
            print("该锻炼了")
        elif bmi < 18.5:
            print("好好吃饭")
        else:
            print("体重正常")

    def run(self):
        print("%s 正在奔跑" % self.name)


if __name__ == '__main__':
    xiaobai = Dog(0.3, 5, 1, "小白")
    xiaobai.breathe()
    xiaobai.say()
    xiaobai.run()

    # 使用类方法来实例化类
    Dog.buy().run()

    Dog.compute_bmi(xiaobai.weight, xiaobai.height)
