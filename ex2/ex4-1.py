import random
import string



if __name__ == '__main__':
    # 密码长度不小于8位，不大于16位。
    # 符包括大小写字母和数字。
    numbers = list(range(48,58))
    letters_low = list(range(65,65+26))
    letters_upper = list(range(97,97+26))
    digist = random.randint(8,16)
    #digist=4
    print("位数："+str(digist))
    s = ""
    s1=0
    for i in range(1,digist+1):
        t = random.randint(1,4)
        if t==1:
            s1 = numbers[random.randint(0,9)]
        elif  t==2:
            s1 = letters_low[random.randint(0, 25)]
        elif t == 3:
            s1 = letters_upper[random.randint(0, 25)]
        s=s+chr(s1)
    print(s)
