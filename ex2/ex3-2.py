def solve_chicken_rabbit(heads, legs):
    # x + y = heads
    # 2x + 4y = legs
    # 解得 y = (legs - 2*heads) / 2
    rabbits = (legs - 2 * heads) // 2
    chickens = heads - rabbits

    # 检查解是否合理
    if rabbits >= 0 and chickens >= 0 and rabbits * 4 + chickens * 2 == legs:
        return chickens, rabbits
    return None, None

if __name__ == '__main__':
    # 解方程组
    heads = 35
    legs = 94
    chickens, rabbits = solve_chicken_rabbit(heads, legs)

    if chickens is not None:
        print(f"鸡有 {chickens} 只，兔有 {rabbits} 只")
    else:
        print("没有符合条件的解")