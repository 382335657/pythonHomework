import math


def P4275_35(t):
    for i in range(t):
        P, S = [int(Y) for Y in input().split()]
        x = math.sqrt((P * P / 4) - 6 * S)
        a1 = ((P / 2) + x) / 6
        a2 = (P / 2 - x) / 6
        b1 = (P / 4) - 2 * a1
        b2 = (P / 4) - 2 * a2
        res = max(a1 * a1 * b1, a2 * b2 * a2)
        print(round(res, 5))


print(P4275_35(int(input())))
