class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"MyClass(name={self.name}, age={self.age})"

    def serialize(self, filename):
        """
        将当前对象的状态保存为二进制文件
        """
        # 将对象的属性转换为字典
        obj_dict = self.__dict__

        # 将字典转换为字节序列
        serialized_data = []
        for key, value in obj_dict.items():
            # 将键和值转换为字节序列
            key_bytes = key.encode('utf-8')
            value_bytes = str(value).encode('utf-8')

            # 将键和值的长度和内容写入
            serialized_data.append(len(key_bytes).to_bytes(4, byteorder='big'))
            serialized_data.append(key_bytes)
            serialized_data.append(len(value_bytes).to_bytes(4, byteorder='big'))
            serialized_data.append(value_bytes)

        # 将所有字节序列拼接起来
        serialized_data = b''.join(serialized_data)

        # 写入文件
        with open(filename, 'wb') as file:
            file.write(serialized_data)

    @classmethod# static
    def deserialize(cls, filename):
        """
        从二进制文件加载对象的状态并创建新的实例
        """
        # 读取文件内容
        with open(filename, 'rb') as file:
            serialized_data = file.read()

        # 初始化一个字典来存储属性
        obj_dict = {}

        # 解析字节序列
        index = 0
        while index < len(serialized_data):
            # 读取键的长度
            key_len = int.from_bytes(serialized_data[index:index + 4], byteorder='big')
            index += 4

            # 读取键
            key = serialized_data[index:index + key_len].decode('utf-8')
            index += key_len

            # 读取值的长度
            value_len = int.from_bytes(serialized_data[index:index + 4], byteorder='big')
            index += 4

            # 读取值
            value = serialized_data[index:index + value_len].decode('utf-8')
            index += value_len

            # 将键值对存入字典
            obj_dict[key] = value

        # 创建类实例并设置属性
        obj = cls(name=None, age=None)
        obj.__dict__.update(obj_dict)

        return obj
if __name__ == '__main__':
    #创建一个类实例
    # obj = MyClass(name="Alice", age=30)
    #
    # # 保存为二进制文件
    # obj.serialize('my_class.bin')

    # 从二进制文件加载
    loaded_obj = MyClass.deserialize('my_class.bin')

    # 打印加载的实例
    print(loaded_obj)  # 输出：MyClass(name=Alice, age=30)