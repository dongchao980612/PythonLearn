import random
import string


if __name__ == '__main__':
    length = random.randint(8, 16)
    print("位数：" +str(length))
    # 定义字符集：大小写字母和数字
    characters = string.ascii_letters + string.digits

    # 从字符集中随机选择字符，生成密码
    password = ''.join(random.choices(characters, k=length))

    print(password)



