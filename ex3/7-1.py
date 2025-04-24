if __name__ == '__main__':
    try:
        # 尝试打开并读取文件
        with open(r"./荷塘月色.txt", "r",encoding="utf-8") as file:
            content = file.read()

        print("文件内容：")
        print(content)
        # print("文件读取成功！")

    except FileNotFoundError:
        print("错误：文件不存在！")
    except IOError:
        print("错误：文件读取过程中发生错误！")
    finally:
        print("文件操作完成！")