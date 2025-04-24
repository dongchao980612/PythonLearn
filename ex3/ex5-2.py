if __name__ == '__main__':

    with open("./test.txt","r+") as f:
        for i in range(1,11):
            f.seek(i*100*5-5)
            t = int(f.readline())
            f.seek(i * 100 * 5 - 5)
            f.write(str(t+1))
            print(i*100*5,t,str(t+1))