if __name__ == '__main__':
    list1 = ['physics', 'chemistry', 1997, 2000]
    list2 = [1, 2, 3, 4, 5, 6, 7]
    other_list=[1,3,5,"hello"]
    # # 加法
    # print("加法")
    # print(list1+other_list)
    # print(list2+other_list)
    # # 乘法
    # print("乘法")
    # print(list1*3)
    # print(list2*3)

    # 添加 append
    print("添加 append")
    list1.append("add one")
    list1.append(2025)
    list1.append(["a","other",'list'])
    print(list1)
    # 添加 insert
    print("添加 insert")
    list1.insert(3,'insert')
    list1.insert(3,2025)
    print(list1)