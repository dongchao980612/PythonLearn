def solve_chicken_rabbit(heads, legs):
    # 遍历可能的鸡的数量
    for chickens in range(heads + 1):
        rabbits = heads - chickens  # 兔子的数量
        total_legs = chickens * 2 + rabbits * 4  # 总脚数

        # 如果总脚数符合条件，就返回结果
        if total_legs == legs:
            return chickens, rabbits

    # 如果没有找到解，返回None
    return None, None

if __name__ == '__main__':
    # 枚举法（暴力解法）
    # 给定的条件
    heads = 35
    legs = 94

    # 调用函数并获取结果
    chickens, rabbits = solve_chicken_rabbit(heads, legs)

    # 输出结果
    if chickens is not None:
        print(f"鸡有 {chickens} 只，兔有 {rabbits} 只")
    else:
        print("没有符合条件的解")