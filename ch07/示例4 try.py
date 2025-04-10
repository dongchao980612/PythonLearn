#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# Time    : 2025/4/10 18:37
# File    : 示例3 try.py
# Software: PyCharm

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2025/4/10 18:31
# File    : 示例2 try.py
# Software: PyCharm

if __name__ == '__main__':
    try:
        print(1/0)
        print(0 + "0")
        print("这里可能会发生异常!!")
    # except Exception  :
    #     print("程序发生了异常！")
    except Exception as e :
        print("程序发生了异常！",e)

