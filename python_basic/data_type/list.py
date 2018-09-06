if __name__ == '__main__':
    # python用方括号来表示列表
    colors = ["1red", "2blue", "3yellow", "4black"]
    print(colors)

    # 下标从0开始. 为什么? 因为代表偏移量
    print(colors[0])

    # 改
    colors[0] = "green"
    print(colors[0])

    # 增
    colors.append("red")
    print(colors)

    # 插
    colors.insert(2, "5purple")
    print(colors)

    # 删
    colors.pop(0)
    print(colors)

    # 出栈
    colors.pop()
    print(colors)

    # 按值删除
    colors.remove("3yellow")
    print(colors)

    # 排序
    colors.sort()
    print(colors)

    # 倒序排列
    colors.sort(reverse=True)
    print(colors)

    # 获得排序后的新列表,原列表顺序不变
    colors_with_sorted = sorted(colors)
    print(colors)
    print(colors_with_sorted)

    # 翻转列表
    colors.reverse()
    print(colors)

    # 获得长度
    print(len(colors))

    # 遍历列表
    for color in colors:
        print(color)

    # 创建数值列表
    values = range(5)
    print(values)
    values = list(values)
    print(values)

    for value in values:
        print(value)

    # 指定范围
    values = range(1, 5 + 1)
    for value in values:
        print(value)

    # 输出1到20的平方
    for value in range(1, 20 + 1):
        _square = value ** 2
        print(_square)

    # min,max,sum
    numbers = range(30)
    print(min(numbers))
    print(max(numbers))
    print(sum(numbers))

    # 复杂列表的生成
    numbers = [number ** 3 for number in range(1, 11)]
    print(numbers)

    # 列表的切片
    numbers = list(range(30))
    print(numbers[3:8])
    print(numbers[:3])
    print(numbers[3:])
    print(numbers[-3:])
    print(numbers[:-3])
    print(numbers[:])

    # 列表的浅拷贝
    numbers = list(range(1, 3 + 1))
    print(numbers)
    numbers_shallow_copy = numbers
    numbers_shallow_copy[2] = 5
    print(numbers)
    print(numbers_shallow_copy)

    # 列表的深拷贝
    numbers = list(range(1, 3 + 1))
    print(numbers)
    numbers_deep_copy = numbers[:]
    numbers_deep_copy[1] = 10
    print(numbers)
    print(numbers_deep_copy)
