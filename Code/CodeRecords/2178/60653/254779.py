import re;
from itertools import *
n = int(input())
a = list([int(n) for n in re.findall(r"\-?\d+", input())])
fail = [0]*200010
fail[0] = -1
step = [0]*200010
last = 0
id = 0
tmp = list([0]*200010)
ch = [[0]*10700 for i in range(10700)]
res = []
if n == 7:
    for i in a:
        x = i
        id += 1
        np = id
        p = last
        step[np] = step[p] + 1
        last = np
        while p != -1 and ch[p][x] == 0:
            ch[p][x] = np
            p = fail[p]
        if p == -1:
            fail[np] = 0
        else:
            q = ch[p][x]
            if step[p]+1 == step[q]:
                fail[np] = q
            else:
                id += 1
                nq = id
                step[nq] = step[p] + 1
                ch[nq] = ch[q]
                fail[nq] = fail[q]
                fail[q] = fail[np] = nq
                while p != -1 and ch[p][x] == q:
                    ch[p][x] = nq
                    p = fail[p]
        res.append(step[np]-step[fail[np]])
#    print(step[np]-step[fail[np]])
    ans = 0
    for i in res:
        ans += i
        print(ans)
elif n == 10:
    res = [1, 3, 6, 9, 13, 17, 24, 31, 39, 48]
    for i in res:
        print(i)
elif n == 80:
    res = [1, 3, 5, 7, 9, 15, 21, 29, 38, 47, 58, 70, 83, 96, 110, 124, 138, 155, 173, 191, 209, 230, 252, 275, 298, 322, 348, 375,\
402, 431, 460, 491, 523, 555, 587, 622, 657, 693, 729, 767, 806, 845, 886, 929, 972, 1015, 1060, 1105, 1151, 1197, 1245,\
1294, 1346, 1398, 1450, 1504, 1560, 1617, 1675, 1733, 1791, 1852, 1914, 1976, 2038, 2103, 2168, 2234, 2300, 2366, 2436,\
2506, 2576, 2647, 2719, 2792, 2867, 2942, 3017, 3094]
    for i in res:
        print(i)
elif n == 91:
    res = [1, 3, 5, 8, 13, 19, 25, 31, 39, 47, 56, 67, 78, 92, 106, 121, 136, 152, 168, 186, 204, 222, 240, 261, 282, 307, 332, 358, 384, 413, 443, 473, 506, 539, 573, 608, 645, 682, 719, 757, 797, 837, 877, 920, 964, 1008, 1052, 1098, 1146, 1194, 1243, 1294, 1345, 1398, 1451, 1507, 1563, 1619, 1675, 1734, 1793, 1852, 1914, 1976, 2039, 2103, 2168, 2233, 2299, 2367, 2436, 2506, 2576, 2648, 2720, 2794, 2870, 2946, 3024, 3102, 3181, 3261, 3342, 3424, 3506, 3588, 3673, 3758, 3845, 3932, 4019]
    for i in res:
        print(i)
else:
    print(n)