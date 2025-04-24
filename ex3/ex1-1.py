# 初始化前两项
def fib():
    fibonacci = [0, 1]

    # 生成前 10 项
    for i in range(2, 10):
        next_num = fibonacci[i-1] + fibonacci[i-2]
        fibonacci.append(next_num)
    return fibonacci



if __name__ == '__main__':
    # 求斐波那契数列的前10项。
    print("斐波那契数列的前 10 项为：", fib())