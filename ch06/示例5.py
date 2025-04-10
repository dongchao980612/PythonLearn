if __name__ == '__main__':
    modes=["r","w","a","r+","w+","a+"]

    for index,mode in enumerate(modes):
        try:
            f = open(f"f_{index + 1}.txt", mode)
        except  Exception as e:
            print(e,mode)



