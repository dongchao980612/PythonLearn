def main():                       # def是用来定义函数的Python关键字
    if __name__ == '__main__':    # 选择结构，识别当前运行方式
        print('This program is run directly.')
    elif __name__ == 'ch01':     # 冒号、换行、缩进表示一个语句块的开始
        print('This program is used as a module.')




if __name__ == '__main__':
    print("hello world")
    main() # 调用上面定义的函数

    exit(0)
    # 注释 以#号开头,不参与程序的运行

    # 不同层级之间的代码差一个tab，不是是个空格

    # 输入输出
    # input() 输入
    a = input()
    print(a)

    a = input("请输入：")
    print("你输入是：",a)

    # 输出
    print("hello")
    print("hello","world","python") # hello world python
    print("hello","world","python",sep="***") # hello***world***python
    print("hello","world","python",end="") # hello***world***python
    print("*******")
    
    name = "张三"
    print("姓名:",name) # 姓名: 张三

    my_name = input("请输入姓名：")
    print("你好，",my_name,"！")

    print("*")
    print("**")
    print("***")
    print("****")
    print("*****")

    
    print("*")
    print("*"*2)
    print("*"*3)
    print("*"*4)
    print("*"*5)