class Person():
    def __init__(self,Name,Age):
        self.name=Name
        self.age=Age
    def main(self):
        print("姓名：",self.name)
        print("年龄：",self.age)

if __name__ == '__main__':
    p=Person("sundy",22)
    p.main()
