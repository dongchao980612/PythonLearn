# 编写程序用于判断输人的年份是否为闰年，
# 判断条件是能被400整除或者被4整除但不被100整除的年份是闰年。

def is_leap_year(year):
    """判断是否为闰年"""
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    return False


def main():
    while True:
        try:
            # 输入年份
            user_input = input("请输入一个年份（输入'q'退出）: ")

            # 如果用户输入'q'，退出程序
            if user_input.lower() == 'q':
                print("程序已退出。")
                break

            # 将输入转换为整数
            year = int(user_input)

            # 检查年份是否为负数
            if year < 0:
                print("年份不能为负数，请重新输入。")
                continue

            # 判断是否为闰年并输出结果
            if is_leap_year(year):
                print(f"{year} 是闰年")
            else:
                print(f"{year} 不是闰年")

        except ValueError:
            # 捕获非整数输入的异常
            print("输入无效，请输入一个有效的整数年份。")
        except Exception as e:
            # 捕获其他异常
            print(f"发生错误: {e}")


if __name__ == "__main__":
    main()

