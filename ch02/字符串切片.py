if __name__ == '__main__':

    my_str="python"
    # 1.a[i:j] i、j 不缺省
    print("1.a[i:j] i、j 不缺省")
    # [1:3]
    print(my_str[1:3])# th
    # [1:-1]
    print(my_str[1:-1])# ytho
    # [-3:-1]
    print(my_str[-3:-1])# ho


    # 1.a[i:j] i、j 缺省
    print("1.a[i:j] i、j 缺省")
    # [:-1]
    print(my_str[:-1])#pytho
    # [-1:]
    print(my_str[-1:])# n
    # [3:]
    print(my_str[3:])# hon
    # [:]
    print(my_str[:])# python

    # 2.a[i:j:k] i，j 不缺省
    print("a[i:j:k] i，j 不缺省")

    # [1:5:2]
    print(my_str[1:5:2])# yh
    # [-1:-3:-2]
    print(my_str[-1:-3:-2])# n


    # 2.a[i:j:k] i，j 缺省
    print("a[i:j:k] i，j 缺省")
    # [::]
    print(my_str[::])# python

    # [1::2]
    print(my_str[1::2])# yhn

    # [:4:2]
    print(my_str[:4:2])# o

    # [::-1]
    print(my_str[::-1])# nohtyp

    # [-1::-2]
    print(my_str[-1::-2])#nhy

    # [:-5:-2]
    print(my_str[:-5:-2])#nh



    # 3.总结