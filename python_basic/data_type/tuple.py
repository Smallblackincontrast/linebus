if __name__ == '__main__':
    # 和列表类似,但是长度固定,且不能被修改
    colors = ("red", "blue")
    for color in colors:
        print(color)

    # 会出现错误,元组不能被修改
    colors[1] = "yellow"

    # 重新赋值是可以的
    colors = ("purple", "green")
    for color in colors:
        print(color)
