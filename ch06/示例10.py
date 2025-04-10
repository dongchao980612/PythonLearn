if __name__ == '__main__':
    f=open("demo.txt","a+",encoding="utf-8")
    str = "\n我对学习python很痴迷"
    f.write(str)
    f.close()
    f=open("demo.txt","r",encoding="utf-8")
    str = f.read()
    print(str)
    f.close()