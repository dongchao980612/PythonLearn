from PIL.ImageFile import StubImageFile


class Student:
    def __init__(self,id,name,score):
        self.id=id
        self.name=name
        self.score = score
    def get_score(self):
        return  self.score
    def __str__(self):
        return f"{self.id,self.name,self.score}"

if __name__ == '__main__':

    stu1=Student("a1001","张大山",92)
    stu2=Student("a1002","李小莉",82)
    stu3=Student("a1003","赵志勇",97)


    print(stu1)
    print(stu2)
    print(stu3)
    s = (stu1.get_score()+stu2.get_score()+stu3.get_score()) /3
    print(int(s))