# class A():
#     def  __init__(self,x,y):
#         self._x = x
#         self.__y = y
class A():
    def  __init__(self,x,y):
        self.x = x
        self.y = y
class B():
    def __init__(self,z):
        self.z = z
class C(A,B):
    def __init__(self, q, x, y,z):
        A.__init__(self,x, y)
        B.__init__(self,z)
        self.q=q
# class AA(A):
#     def __init__(self, a, x, y):
#         super().__init__(x, y)
#         self.a = a


if __name__ == '__main__':
    # a = A(1,2)
    # print(a._x)
    # # print(a.__y)
    # print(a._A__y)
    #
    # a=AA(1,2,3)
    # aa=AA(1,2,3)
    c = C(1,2,3,4)
