from ch03.Person import Person


class Sunny(Person):
    def __init__(self,name,age,score):
        super(Sunny,self).__init__(age,name)
        self.score = score
    def prn(self):
        Person.main(self)
        print("成绩：",self.score)

if __name__ == '__main__':
    s=Sunny("张大山",28,88)
    s.prn()