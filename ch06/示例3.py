import shutil

if __name__ == '__main__':
    import os

    #  加入test.txt
    path = ".\\mqtt2\\web2"
    path1 = ".\\mqtt3\\web3"

    # os.rmdir(path)
    shutil.rmtree(path1)
