if __name__ == '__main__':
    # 相等与赋值
    test_number = 1
    print(test_number)
    print(test_number == 1)
    print(test_number == 2)

    # 不相等
    test_number = 1
    print(test_number != 1)

    # >,<,>=,<=

    # and 判断多个条件
    test_number = 2
    print(test_number > 0 and test_number > 1)
    print(test_number > 0 and test_number > 2)

    # or 满足一个即可
    test_number = 2
    print(test_number > 0 or test_number > 1)
    print(test_number > 0 or test_number > 2)

    # 特定值是否在列表中
    print(2 in range(0, 5))
    print(6 in range(0, 5))

    # 布尔表达式
    bool_demo = True
    print(bool_demo == True)
    print(bool_demo == False)
