if __name__ == '__main__':
    str="Hello Python\n向文件写入数据"
    f=open("demo.txt","w",encoding="utf-8")
    f.write(str)
    f.close()