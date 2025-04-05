if __name__ == '__main__':
    # 字符串
    x = 'Hello world.'  # 使用单引号作为定界符
    x = "Python is a great language."  # 使用双引号作为定界符
    x = '''Tom said, "Let's go."'''  # 不同定界符之间可以互相嵌套
    print(x)

    x = 'good ' + 'morning'  # 连接字符串
    print(x)

    x = 'good ''morning'  # 连接字符串，仅适用于字符串常量
    print(x)

    x = 'good '
    # x = x'morning'  # 不适用于字符串变量
    # SyntaxError: invalid syntax

    x = x + 'morning'  # 字符串变量之间的连接可以使用加号
    print(x)