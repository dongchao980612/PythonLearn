


if __name__ == '__main__':



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

