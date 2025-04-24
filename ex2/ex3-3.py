import numpy as np


def solve_chicken_rabbit(heads, legs):
    # 方程组系数矩阵
    A = np.array([[1, 1], [2, 4]])
    # 常数项
    b = np.array([heads, legs])

    try:
        # 解线性方程组
        x = np.linalg.solve(A, b)
        chickens, rabbits = x
        # 检查解是否合理
        if chickens >= 0 and rabbits >= 0 and chickens.is_integer() and rabbits.is_integer():
            return int(chickens), int(rabbits)
    except np.linalg.LinAlgError:
        pass
    return None, None

if __name__ == '__main__':


    heads = 35
    legs = 94
    chickens, rabbits = solve_chicken_rabbit(heads, legs)

    if chickens is not None:
        print(f"鸡有 {chickens} 只，兔有 {rabbits} 只")
    else:
        print("没有符合条件的解")