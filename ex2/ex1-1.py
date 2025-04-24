# 编写程序用于判断输人的年份是否为闰年，
# 判断条件是能被400整除或者被4整除但不被100整除的年份是闰年。



if __name__ == "__main__":
    year = int(input("请输入一个年份: "))
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(year,"是闰年")
    else:
        print(year, "不是闰年")
