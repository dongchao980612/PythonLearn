if __name__ == '__main__':
    # 以二进制模式写入文件
    with open('output.bin', 'wb') as file:
        binary_data = bytes([120, 3, 255, 0, 100])
        file.write(binary_data)

    # 以二进制模式读取文件
    with open('output.bin', 'rb') as file:
        binary_data = file.read()
        print(binary_data)
        print(binary_data.hex())

    # with open('my_class.bin', 'rb') as file:
    #     binary_data = file.read()
    #     print("my_class=",binary_data)
    #     print("my_class=",binary_data.hex())





