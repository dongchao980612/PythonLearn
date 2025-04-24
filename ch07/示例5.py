if __name__ == '__main__':
    while True:
        x = input('Please input:')
        try:
            x = int(x)
            print('You have input',x)
            break
        except Exception as e:
            print(e)
