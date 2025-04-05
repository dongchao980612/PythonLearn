class A:
    def __init__(self):
        self.one="第一个父类"
class B:
    def __init__(self):
        self.two="第二个父类"
class C(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
    def prn(self):
        print(self.one,"\n",self.two)



if __name__ == '__main__':
    subc=   C()
    subc.prn()