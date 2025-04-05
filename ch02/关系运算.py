if __name__ == '__main__':
    print(3<5)# True
    print(4!=7)# True
    a=4
    print(a==5)# False
    print(2 < a < 6 < 8)# True  T+T+T
    print(2 < a == 4 < 8)# True T+T+T
    print(2 < a == 5 < 8)# False T+F+T
    print((2 < a) == (7<8))# True T+T
    print(2<a>5)# False T+F
    b=a<=6# True
    print(b)# True