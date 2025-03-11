if __name__ == '__main__':
    # 构造字符串
    s1 = str(12581)# 构造字符串
    print(type(s1))

    # 字符串计数(count，len)
    str = "my name is qlee, what is your name?"
    print(str.count("name"))  # 2
    print(len(str))  # 35

    # 查询（index，find）
    str1 = "my name is qlee, my name is nice, what your name?"
    str2 = "name"

    print(len(str1))  # 49
    print(str1.find(str2))  # 全部查找
    print(str1.find(str2, 5))  # 从第5个元素开始查找
    print(str1.rfind(str2, 5))  # 从第5个元素开始查找，超过元素索引或者没找到，不会报错

    print(str1.index(str2))  # 全部查找
    print(str1.index(str2, 5))  # 从第5个元素开始查找
    print(str1.rindex(str2, 5))  # 从第5个元素开始查找，超过元素索引或者没找到，不会报错
    # 建议使用find，因为如果没有找到匹配的字符串，index方法会报异常
    # ValueError: substring not found


    # 字符串大小写转换操作
    txt = "my name is Qlee"
    print(txt.upper())# 大写
    print(txt.lower())# 小写
    print(txt.swapcase())# 交换
    print(txt.capitalize())# 首句首字母大写
    print(txt.title())# 首字母大写

    # 分割字符串(split、splitlines和partition)
    str = "my name is qlee, what is your name"
    print(str.split())  # 以空格为分隔符
    print(str.split('i', 1))  # 以 i 为分隔符
    print(str.split('b'))  # 以b为分隔符,没找到不会报错
    print(str.partition("name"))  # 找到第一个name，分割为三部分
    print(str.rpartition("name"))  # 反向找到第一个name，分割为三部分

    str = """my name is qlee
          what is your name"""
    print(str.splitlines())# 按照行进行分割，得到新的列表

    # 替换(join，replace)
    str1 = "my name is qlee"
    print(str1.replace("qlee", "lq"))  # 注意str1本身不发生改变


    # 判断字符串(isidentifier、isspace、isalpha、isdecimal、isnumeric和isalnum等)
    print("hello&".isidentifier())  # False,&为非法标识符
    print("   t".isspace())  # False,"t"为非空
    print("aldflafd你好".isalpha())  # ture,中文也可以
    print("123四".isdecimal())  # False,中文不属于十进制
    print("123四".isnumeric())  # True,中文、罗马字符的数字也算
    print("123abc".isalnum())  # True,只能字母和数字
    print("123四".isdigit())  # False，不能包括中文
    print("".islower())  # False,不能为空字符
    print("TLUHBH".isupper())  # True
    print("My Name Is Qlee".istitle())  # True,只有第一个字符为大写
    print("我是中国人".isascii())  # False，中文不属于ascii
    print("Hello!\nAre you ?".isprintable())  # False,\n不可打印

    # 去除两端多余字符操作(strip)
    str = "   my name is qleeeeee"
    print(str.strip())  # 去掉两边的空白
    print(str.rstrip("e"))  # 去掉右边的"e"字符
    str = "!!!!my name is qlee!!!!"
    print(str.strip("!"))  # 去掉左右边的"!"字符

    # 判断开头结尾字符串(startswith，endswith)
    str = "my name is qlee"
    print(str.startswith("my"))  # True
    print(str.endswith("is"))  # False



    # 字符串的编码与解码(encode，decode)
    str = "我是中国人"
    str_utf8 = str.encode("UTF-8")
    str_gbk = str.encode("GBK")

    print("原字符串：", str)
    print("------------编码---------------")
    print("UTF-8 编码：", str_utf8)
    print("GBK 编码：", str_gbk)
    print("------------解码---------------")
    print("UTF-8 解码：", str_utf8.decode('UTF-8', 'strict'))
    print("GBK 解码：", str_gbk.decode('GBK', 'strict'))

    str = "我是中国人"
    print("中国人" in str)
    print("外国人" not in str)








