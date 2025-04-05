class TestPrivate():
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
        self.__s=0
    def add(self):
        self.__s = self.__x+self.__y
        return self.__s
    def printData(self):
        print(self.__s)

if __name__ == '__main__':
    t=TestPrivate(3,4)
    t.printData()
    print("s = ",t.add())
