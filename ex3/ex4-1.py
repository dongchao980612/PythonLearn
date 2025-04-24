if __name__ == '__main__':
    # 初始化计数器
    count = 0

    # 打开并读取文件
    with open(r"./test424.txt", "r") as file:
        for line in file:
            # 去除行末的换行符并转换为整数
            num = int(line.strip())
            # 判断个位数是否为5
            if num % 10 == 5:
                count += 1

    print(f"文件中个位数为5的数字的个数为：{count}")