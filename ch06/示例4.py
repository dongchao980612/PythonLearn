if __name__ == '__main__':
    import shutil

    old_path = "./old_path/old"
    new_path = "./new_path"  # 必须不存在

    shutil.copytree(old_path, new_path)
