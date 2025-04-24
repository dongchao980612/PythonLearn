if __name__ == '__main__':
    try:
        with open("ceshi3.txt","r+") as f:
            print(f.read())
    except Exception as e:
        print(e)
