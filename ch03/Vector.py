class Vector:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __str__(self):
        return f"Vector ({self.a},{self.b})"
    def __add__(self, other):
        return f"Vector ({self.a+other.a},{self.b+other.b})"
    def __sub__(self, other):
        return f"Vector ({self.a-other.a},{self.b-other.b})"
if __name__ == '__main__':
    v1=Vector(7,10)
    v2=Vector(5,-2)
    print(v1+v2)
    print(v1-v2)