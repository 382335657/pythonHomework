n, k = map(int, input().split())
leave = list(map(int, input().split()))
cnt = 0
res = []
time = set()
for x in range(n):
    res.append(0)
while max(leave) > 0:
    index = leave.index(max(leave))
    now = index + 1
    while now <= k:
        now = now + 1
    while now in time:
        now = now + 1
    res[index] = now
    time.add(now)
    #print(now)
    cnt = cnt + (now - index - 1)*leave[index]
    leave[index] = -1
print(cnt)
i = 0
for x in leave:
    if leave.index(x) != i:
        tem = res[leave.index(x)]
        res[leave.index(x)] = res[i]
        res[i] = res[leave.index(x)]
    i = i + 1
for i in range(len(res)):
    print(res[i],end = " ")