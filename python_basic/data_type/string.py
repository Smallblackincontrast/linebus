if __name__ == '__main__':
    # python使用类型推导式的变量定义方式
    message = "Hello python world!"

    # 使用 + 号,来拼接字符串
    print("This is the first variable definition : " + message)

    # String的定义可以使用单引号,或者双引号,这取决于字符串本身的内容

    # 如果字符串中包含单引号,那我们用双引号来定义
    single_quote_definition_string = "XiaoXue's dog"

    # 如果字符串中包含双引号,那我们用单引号来定义
    double_quotes_define_string = 'document.getElementById("anyControlId")'

    # 如果字符串中同时包括单引号和双引号,使用转义符 \ 来解决
    escape_character_string = "XiaoXue's dog.document.getElementById(\"anyControlId\")"

    # 转义符还可以用于输出特殊符号,比如换行,回车,Tab等
    escape_character_output_special_symbol = "后面会换行.\n\r然后A\tB之间有个Tab "
    print(escape_character_output_special_symbol)

    # 一些字符串函数
    demo_string = "    hello python world  "
    capitalize_the_first_letter = demo_string.title()
    print(capitalize_the_first_letter)

    # 变全大写
    all_uppercase = demo_string.upper()
    print(all_uppercase)

    # 变全小写
    all_lowercase = demo_string.lower()
    print(all_lowercase)

    # 删除左侧空白
    remove_left_margin = demo_string.lstrip()
    print(remove_left_margin)

    # 删除右侧空白
    remove_right_margin = demo_string.rstrip()
    print(remove_right_margin)

    # 删除两侧空白
    remove_both_sides_of_the_blank = demo_string.strip()
    print(remove_both_sides_of_the_blank)
