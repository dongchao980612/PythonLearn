import random
if __name__ == '__main__':

    # 随机生成 1000 个 100 到 999 之间的整数
    random_numbers = [random.randint(100, 999) for _ in range(1000)]

    # 将每个整数写入文件，每个整数占一行
    with open(r"./test424.txt", "w") as file:
        for number in random_numbers:
            file.write(f"{number}\n")

    print("随机生成的 1000 个整数已成功写入 test.txt 文件中。")