if __name__ == '__main__':
    lst=["MSN","wechat","QQ","OICQ"]


    for i in lst:
        print(i,end=" ")

    print()
    for i in  range(len(lst)):
        print(i,lst[i],end=" ")
    print()
    for i,v in enumerate(lst):
        print(i,v)





    print()
    for i in "hello":
        print(i,end=" ")
    print()
    # for循环示例

    # 使用序列迭代法 显示列表 ["xyz","book","hello"]
    # 使用序列索引迭代法 显示列表 ["C++","Java","Python"]
    # 使用数字迭代法 显示5个数字





    num = list(range(2,101,2))
    S = 0
    for i in num:
        S = S+i
        # print(i)
    print(S)