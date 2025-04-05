class Mood:
    def __init__(self,x):
        self.x=x
        print("产生对象",self.x)
    def __del__(self):
        print("销毁对象",self.x)

if __name__ == '__main__':
    m1=Mood(1)
    m2=Mood(2)
    del m1,m2
