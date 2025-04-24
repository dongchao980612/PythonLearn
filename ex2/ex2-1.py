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
    for i in range(end_Num):
        total +=m[i]/d[i]

    print(float(total))
