if __name__ == '__main__':
    # 任意两个整数，按照从小到大的顺序依次输出
    # a = int(input("输入第一个数："))
    # b = int(input("输入第二个数："))
    # print("排序前：",a, b)
    # if a>b:
    #     # 交换两个数x
    #     a,b=b,a
    # print("排序后：", a, b)


    # 计算
    '''
    y= x^2-25  ,   x<=-1 或者 x>=5
        25-x^2 ,  -5<x<5
    '''
    x=float(input("请输入一个数字"))
    if 5<x and x>-5:
        y = x**2-25
    else:
        y = 25-x**2
    print(y)

