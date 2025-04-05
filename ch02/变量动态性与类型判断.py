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
