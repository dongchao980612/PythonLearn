from fractions import Fraction

if __name__ == '__main__':

    end_Num = 6
    m = [2, 3]  # 分子数列
    d = [1, 2]  # 分母数列

    for i in range(2, end_Num):
        m_next = m[i-1] + m[i-2]
        m.append(m_next)
        d_next = d[i-1] + d[i-2]
        d.append(d_next)

    print(m)
    print(d)

    total=0
    # 计算前20项的和
    total = Fraction(0, 1)
    for i in range(end_Num):
        total += Fraction(m[i], d[i])

    # 输出结果（可选：转换为浮点数）
    print(float(total))