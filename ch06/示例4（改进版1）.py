if __name__ == '__main__':
    import os
    import shutil

    old_path = "./old_path/old"
    new_path = "./new_path"  # 必须不存在
    isExits = os.path.exists(new_path)
    if isExits:
        shutil.rmtree(new_path)

    isExits = os.path.exists(old_path)
    if isExits:
        shutil.copytree(old_path, new_path)
        print("文件夹"+old_path+"复制到"+new_path+"成功")
    else:
        print(old_path+"目录不存在")




