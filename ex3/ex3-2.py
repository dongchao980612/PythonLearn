import random
if __name__ == '__main__':


    # 将每个整数写入文件，每个整数占一行
    with open(r"./test1.txt", "w") as file:
        for number in range(1000):
            file.write(f"{str(random.randrange(100,999))}\n")

    print("随机生成的 1000 个整数已成功写入 test1.txt 文件中。")