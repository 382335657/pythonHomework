num = int(input())
for i in range(num):
    m = list(map(int, input().split(" ")))  # 反向考虑不相交的情况
    n = list(map(int, input().split(" ")))
    m_x, m_y, n_x, n_y = m[0], m[1], n[0], n[1]
    m_width, m_height = m[2] - m[0], m[1] - m[3]
    n_width, n_height = n[2] - n[0], n[1] - n[3]
    if m_x + m_width > n_x and n_x + n_width > m_x and m_y > n_y + n_height and n_y > m_y + m_height:
        print(1)
    else:
        print(0)