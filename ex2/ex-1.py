def count_characters(text):
    # 创建一个空字典来存储字符计数
    char_count = {}

    # 遍历文本中的每个字符
    for char in text:
        # 如果字符已经在字典中，增加计数
        if char in char_count:
            char_count[char] += 1
        # 如果字符不在字典中，初始化计数为1
        else:
            char_count[char] = 1

    return char_count

if __name__ == '__main__':

    # 输入文本
    text = input("请输入英文文本: ")

    # 调用函数并获取结果
    result = count_characters(text)

    # 按字符的ASCII码值排序并输出结果
    sorted_result = sorted(result.items(), key=lambda x: ord(x[0]))
    for char, count in sorted_result:
        print(f"字符 '{char}': {count} 次")

    # 如果需要统计不区分大小写的版本，可以将文本转换为小写或大写
    # print("\n不区分大小写的统计结果:")
    # lowercase_text = text.lower()
    # lowercase_result = count_characters(lowercase_text)
    # sorted_lowercase_result = sorted(lowercase_result.items(), key=lambda x: ord(x[0]))
    # for char, count in sorted_lowercase_result:
    #     print(f"字符 '{char}': {count} 次")