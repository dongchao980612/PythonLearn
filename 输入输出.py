if __name__ == '__main__':
    # 输入输出
    # input() 输入
    a = input()
    print(a)

    a = input("请输入：")
    print("你输入是：", a)

    # 输出
    print("hello")
    print("hello", "world", "python")  # hello world python
    print("hello", "world", "python", sep="***")  # hello***world***python
    print("hello", "world", "python", end="")  # hello***world***python
    print("*******")

    name = "张三"
    print("姓名:", name)  # 姓名: 张三

    my_name = input("请输入姓名：")
    print("你好，", my_name, "！")

    print("*")
    print("**")
    print("***")
    print("****")
    print("*****")

    print("*")
    print("*" * 2)
    print("*" * 3)
    print("*" * 4)
    print("*" * 5)