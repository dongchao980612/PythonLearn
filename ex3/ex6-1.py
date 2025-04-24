if __name__ == '__main__':
    try:
        # 获取用户输入
        num1 = float(input("请输入第一个数字："))
        num2 = float(input("请输入第二个数字："))

        # 执行除法运算
        result = num1 / num2
    except ValueError:
        print("输入错误：请输入有效的数字！")

    except ZeroDivisionError:
        print("错误：除数不能为零！")

    else:
        print(f"结果：{result}")
        print("计算完成！")

    finally:
        print("感谢您的使用！")