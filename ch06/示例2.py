if __name__ == '__main__':
    import os

    path = ".\\mqtt1\\web1"
    isExists = os.path.exists(path)
    print(isExists)
    if isExists:
        print(path + "已经存在！")
    else:
        os.makedirs(path)  # 创建递归目录
        print(path + "创建成功！")
