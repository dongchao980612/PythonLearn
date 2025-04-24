
def  cal_sum(num):
    sum_digits = 0

    for digit in num:
        sum_digits += int(digit)
    return sum_digits
if __name__ == '__main__':
    num = input("请输入一个数字：")


    print(f"{num} 的各位数字之和为：{cal_sum(num)}")