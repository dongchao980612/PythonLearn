
if __name__ == '__main__':
    # 变量
    x = 3
    print(x)
    print(id(x))

    x = 'Hello world.'
    print(x)
    print(id(x))

    y = x
    print(id(y))


    o_x = 3
    print(id(o_x))

    print(type(3))# <class 'int'>
    print(type(3.10))# <class 'float'>
    print(type(3+2j))# <class 'complex'>
    print(type("hello world"))# <class 'str'>
    print(type(True))# <class 'bool'>

    print(9999 ** 99)
    print(3.9-2.31)# 1.5899999999999999

    print(1_000_000)# 1000000
    print(1_2_3_4)# 1234
    print(1_2 + 3_4j)# (12+34j)
    print(1_2.3_45)# 12.345

    # 字符串
    x = 'Hello world.'  # 使用单引号作为定界符
    x = "Python is a great language."  # 使用双引号作为定界符
    x = '''Tom said, "Let's go."'''  # 不同定界符之间可以互相嵌套
    print(x)

    x = 'good ' + 'morning'  # 连接字符串
    print(x)

    x = 'good ''morning'  # 连接字符串，仅适用于字符串常量
    print(x)

    x = 'good '
    # x = x'morning'  # 不适用于字符串变量
    # SyntaxError: invalid syntax

    x = x + 'morning'  # 字符串变量之间的连接可以使用加号
    print(x)

    # 列表、元组、字典、集合
    x_list = [1, 2, 3]                 # 创建列表对象
    x_tuple = (1, 2, 3)                # 创建元组对象
    x_dict = {'a':97, 'b':98, 'c':99}  # 创建字典对象
    x_set = {1, 2, 3}                  # 创建集合对象
    print(x_list[1])                   # 使用下标访问指定位置的元素

    print(x_tuple[1])                  # 元组也支持使用序号作为下标

    print(x_dict['a'])                 # 字典对象的下标是“键”

    print(3 in x_set )                 # 集合对象支持成员关系测试


    x_str = "hello"
    print(x_str[1])
    print(x_str[-1])

    my_str="python"
    print(my_str[1:4])# yth
    print(my_str[1:4:2])# yh
    print(my_str[1:])# ython
    print(my_str[:4])# pyth
    print(my_str[:4])# pyth
