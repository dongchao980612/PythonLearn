if __name__ == '__main__':
    print(1<2 and 1<3)# True T and T
    print(1<2 and  1 >3)# False T and F
    n=4
    print(n >= 2 and n < 5 and n % 2 == 0)# True
    print(n >= 2 and n < 5 and n % 2 == 1)# False
    print("*"*10)
    print(""==False)# False
    print([]==False)# False
    # 不同类型的对象在比较时，会根据它们的类型进行比较
    print(2==True)# False
    print([2,3]==True)# False
    print("OK"==True)# False
    # 1以外的非0的数、非空字符串、非空列表都不是True
    print(0 and "ok")# 0
    # 当第一个操作数 0 是"假"值时，整个表达式的结果就是
    print(True and 8)# 8
    # 当第一个操作数 True 是"真"值时，整个表达式的结果是第二个操作
    print("*"*10)
    n=4
    print(n>4 or n<5)# True F or F
    print(0 or "ok")# ok
    print("" or [])# []
    print(4 > 5 or 4 >= 2 or 4%2 == 1)# True F or T or F
    print("*" * 10)
    print(not 4 < 5)  # False
    print(not 5)  # False
    print(not 0)  # True
    print(not "abc")# False
    print(not  "")# True
    print(not [])# True
    print(not [1])# False


    # 优先级
    print("*" * 10)
    print(3 + 2 < 5)  # False
    print(3 + (2 < 5))  # 4
    n=4
    a=7<n +3 and n<5
    print(a)  # False

