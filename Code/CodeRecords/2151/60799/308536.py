import sys

inp = input().split()
n, m = int(inp[0]), int(inp[1])
alist = [[] for i in range(n)]
res=0
for kkk in range(m):
    inp = [int(i) for i in input().split()]
    i, j, w = inp[0] - 1, inp[1] - 1, inp[2]
    alist[i].append((j, w))
    alist[j].append((i, w))

visi = [False] * n
inde = [i for i in range(n)]
minl = [sys.maxsize] * n
visi[0] = True
res=0
for i in alist[0]:
    if minl[i[0]] > i[1]:
        minl[i[0]] = i[1]
        inde[i[0]] = 0

for ttt in range(n - 1):
    mindis = sys.maxsize
    indexx = -1
    for iii in range(0, n):
        if not visi[iii]:
            if minl[iii] < mindis:
                indexx = iii
                mindis = minl[iii]
    # print(indexx+1, inde[indexx]+1)
    res += minl[indexx]
    visi[indexx] = True

    for iii in alist[indexx]:
        if not visi[iii[0]]:
            res=262221
            if iii[1] < minl[iii[0]]:
                minl[iii[0]] = iii[1]
                inde[iii[0]] = indexx

print(res)