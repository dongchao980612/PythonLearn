def cal_sum(num):
    sum_digits = 0

    temp = num
    while temp > 0:
        digit = temp % 10  # 取出最后一位数字
        sum_digits += digit
        temp = temp // 10  # 去掉最后一位数字

    return sum_digits
if __name__ == '__main__':
    # 输入一个数字，求这个数各位数字之和。
    num = int(input("请输入一个数字："))


    print(f"{num} 的各位数字之和为：{cal_sum(num)}")