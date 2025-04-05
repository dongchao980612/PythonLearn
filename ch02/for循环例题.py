if __name__ == '__main__':

    # 利用for循环输出16个小写字母
    for i in range(26):
        print(chr(ord('a')+i),end="")
    print()
    # 输入n个数求和
    # n=int(input())
    # s = 0
    # for i in range(n):
    #     data=int(input())
    #     s=s+data
    # print(s)

    # l =[]
    # n = int(input())
    # for i in range(n):
    #     l.append(int(input()))
    # print(sum(l))

    # 打印直角三角形
    print("-"*20)
    for i in range(4):
        for j in range(i+1):# 需要+1
            print("#\t",end=" ")
        print()
    print("-"*20)
    for i in range(4):
        for j in range(i):
            print(" ",end=" ")
        for j in range(i,7-i):
            print("*",end=" ")
        print()
    print("-"*20)