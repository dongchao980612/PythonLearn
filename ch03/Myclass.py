class Person:
    """
    this is my class

    """
    head= 1
    legs=4

    def __init__(self,name,age,wechat,qq):
        print("Person __init__ is running...")
        self.name=name
        self.age=age
        self.__wechat=wechat
        self._qq=qq

    def run(self):
        # print("self:",self.name)
        print("run...")
    def __del__(self):
        print("del....")
class Book:
    def __init__(self,book_name):
        self.book_name=book_name
        print("Book __init__ is running...")

class Teacher(Person,Book):
    def __init__(self,name,age,wechat,qq,sex,book_name):
        Person.__init__(self, name, age, wechat, qq)  # 调用 Person 的 __init__
        Book.__init__(self, book_name)  # 调用 Book 的 __init__
        self.sex = sex

        print("Teacher __init__ is running...")

    # def run(self):
    #     print("run  run...")

    def walk(self):
        print("walk walk ...")

if __name__ == '__main__':
    p1 = Person("p1", 18,"p1 wechat","p1 qq")
    # p2=Person("p2",20,"p2 wecaht","p2 qq")
    # print(p1.head)
    # p1.run()
    # p2.run()
    # print(id(p1),id(p2))
    # print(p1,p2)
    # print(id(p1.legs),id(p2.legs))

    # p1.name="p1"
    # p2.name="p2"
    # p1.run()
    # p2.run()
    # #print(p1.name)
    # # print(p2.name)
    #print(id(p1.name)==id(p2.name))
    # help(Person)
    # print(p1.__wechat)
    # print(p1._qq)
    # print(p1._Person_.wechat)
    t=Teacher(name = "t1", age = 18,wechat = "p1 wechat",qq = "p1 qq", sex="M",book_name="book name")
    print(t.sex,t.book_name)

    #t.run()
    #print(p1.sex) 父类对象无法调用子类属性
    t.run()
    p1.run()

    # t.walk()
    # p1.walk()

    t.run()
    p1.run()
