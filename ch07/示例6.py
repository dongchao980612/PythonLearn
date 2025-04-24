def add_N(a,b):
    # if a<0:
    #     raise ValueError("a必须的大于0")
    if a<0:
        print("a必须的大于0")
        return  None
    return a+b

if __name__ == '__main__':

    # try:
    #     a = input("输入一个数：")
    #     # 判断用户输入的是否为数字
    #     if not a.isdigit():
    #         raise ValueError("a 必须是数字")
    # except ValueError as e:
    #     print("引发异常：", e)

    # try:
    #     add_N(-1, 5)
    # except ValueError as e:
    #     print(e)
    res = add_N(-1,9)
    if res is None :
        print("ufiu23b")
