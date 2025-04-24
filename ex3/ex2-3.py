
def sum_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_digits(n // 10)


if __name__ == '__main__':
    num = int(input("请输入一个数字："))
    print(f"{num} 的各位数字之和为：{sum_digits(num)}")