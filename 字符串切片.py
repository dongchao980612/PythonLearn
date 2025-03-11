if __name__ == '__main__':

    my_str="python"
    # 1.a[i:j] i、j 不缺省
    print("1.a[i:j] i、j 不缺省")
    # [1:3] 取第二、三个元素
    print(my_str[1:3])

    # [1:-1] 取第二个到倒数第二个元素
    print(my_str[1:-1])
    
    # [-3:-1] 取倒数第三个到倒数第二个元素
    print(my_str[-3:-1])

    # 1.a[i:j] i、j 缺省
    print("1.a[i:j] i、j 缺省")
    # [:-1] 取第一个到倒数第二个元素
    print(my_str[:-1])

    # [-1:] j缺省，为5，取最后一个元素
    print(my_str[-1:])

    # [3:] j缺省，为5，取第四个到最后一个元素
    print(my_str[3:])

    # [:] 取全部元素
    print(my_str[:])

    # 2.a[i:j:k] i，j 不缺省
    print("a[i:j:k] i，j 不缺省")

    # [1:5:2] 从左往右，步长为2 范围从第二个到最后一个元素
    print(my_str[1:5:2])

    # [-5:-2:2] 从左往右，步长为2 范围从第一个到倒数第二个元素
    print(my_str[1:5:2])

    # [-1:-3:-2] 从左往右，步长为2 范围从第一个到倒数第二个元素
    print(my_str[-1:-3:-2])

    # 2.a[i:j:k] i，j 缺省
    print("a[i:j:k] i，j 缺省")

    # [::] 从左往右 取全部
    print(my_str[::])

    # [1::2] 从左往右 步长为2 范围从第一个到最后一个元素
    print(my_str[1::2])

    # [:4:2] 从左往右 步长为2 范围从第二个到最后二个元素
    print(my_str[:4:2])

    # [[::-1]] 从左往右 步长为2 范围从第二个到最后二个元素
    print(my_str[::-1])

    #
    print(my_str[-1::-2])

    #
    print(my_str[:-5:-2])


    # 3.总结