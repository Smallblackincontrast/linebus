"""
循环的使用
"""
if __name__ == '__main__':
    # 基本循环结构
    current_number = 1
    while current_number <= 5:
        print(current_number)
        current_number += 1

    # 使用continue
    current_number = 0
    while current_number <= 5:
        current_number += 1
        if current_number == 4:
            continue
        print(current_number)

    # 使用break
    current_number = 0
    while current_number <= 5:
        current_number += 1
        if current_number == 4:
            break
        print(current_number)

    # 删除特定元素
    pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
    print(pets)

    while 'cat' in pets:
        pets.remove('cat')

    print(pets)
