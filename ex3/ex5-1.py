if __name__ == '__main__':
    # 读取文件内容
    with open(r"./test424.txt", "r") as file:
        numbers = file.readlines()

    # 将第100, 200, ..., 1000个数加1
    for i in range(99, 1000, 100):  # 索引从0开始，第100个数的索引是99
        numbers[i] = str(int(numbers[i]) + 1) + "\n"

    # 将修改后的内容写回文件
    with open(r"./test424.txt", "w") as file:
        file.writelines(numbers)

    print("文件已修改，第100, 200, ..., 1")