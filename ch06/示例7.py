if __name__ == '__main__':
    f=open("荷塘月色.txt","r",encoding="utf-8")
    while True:
        str = f.readline()
        print(str,end="")
        if not str:
            break
    f.close()