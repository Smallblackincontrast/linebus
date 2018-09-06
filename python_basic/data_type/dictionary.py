if __name__ == '__main__':

    # 定义
    colors = {"red": "红色", "blue": "蓝色", "yellow": "黄色"}
    for color in colors:
        print(color + " 的中文是 " + colors[color])

    # 修改,增加
    colors = {"red": "红色", "blue": "蓝色", "yellow": "黄色"}
    colors['purple'] = '紫色'
    print(colors)

    # 遍历键和值
    colors = {"red": "红色", "blue": "蓝色", "yellow": "黄色"}
    for color in colors:
        print(color + " 的中文是 " + colors[color])

    # 遍历所有的条目
    colors = {"red": "红色", "blue": "蓝色", "yellow": "黄色"}
    for color_key, color_value in colors.items():
        print(color_key + " 的中文是 " + color_value)

    # 单独遍历keys
    colors = {"red": "红色", "blue": "蓝色", "yellow": "黄色"}
    for color_key in colors.keys():
        print(color_key)

    # 单独遍历values
    colors = {"red": "红色", "blue": "蓝色", "yellow": "黄色"}
    for color_value in colors.values():
        print(color_value)

    # 删除
    colors = {"red": "红色", "blue": "蓝色", "yellow": "黄色"}
    del colors['red']
    for color in colors:
        print(color + " 的中文是 " + colors[color])

    # 另一种删除
    colors = {"red": "红色", "blue": "蓝色", "yellow": "黄色"}
    colors.pop('blue')
    for color in colors:
        print(color + " 的中文是 " + colors[color])

    # 数据结构的嵌套
    # 字典中包含列表,或者反过来
    red_color = {"name": "red", "cn": "红色"}
    blue_color = {"name": "blue", "cn": "蓝色"}

    complex_list = [red_color, blue_color]

    for dic in complex_list:
        print(dic["name"] + "的中文是" + dic["cn"])
