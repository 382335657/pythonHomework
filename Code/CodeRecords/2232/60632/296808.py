"""x为当前访问的节点，time为时间戳，n为节点总数"""


def tarjan(x: int, time: int, n: int):
    time += 1
    dfn[x] = low[x] = time
    stack.append(x)
    for y in range(n):
        if adj[x][y] == 1:
            if dfn[y] == 0:
                tarjan(y, time, n)
                low[x] = min(low[x], low[y])
            elif y in stack:
                low[x] = min(low[x], low[y])
    if dfn[x] == low[x]:
        tmp = []
        while stack[-1] != x:
            tmp.append(stack.pop())
        tmp.append(stack.pop())
        result.append(tmp)


n = int(input())
dfn = [0 for i in range(n)]  # dfn[i]表示第i个节点被访问的时间戳
low = [0 for j in range(n)]  # low[i]表示第i个节点可回溯到的最小的时间戳
adj = [[0 for a in range(n)] for b in range(n)]  # 邻接矩阵
stack = []  # 辅助栈
result = []
for i in range(n):
    s = input()
    tmp = []
    try:
        tmp = list(map(int, s.split(' ')))
    except ValueError as e:
        tmp = list(map(int, s.replace('  ',' ').split(' ')))
    for j in range(len(tmp) - 1):
        adj[i][tmp[j] - 1] = 1
for i in range(n):
    if dfn[i] == 0:
        tarjan(i, i, n)
# print(result)
num = len(result)
for i in result:
    judge = False
    for j in i:
        for k in range(n):
            if k not in i and adj[k][j] == 1:
                judge = True
                break
        if judge:
            break
    if judge:
        num -= 1
print(num)
if False:
    pass
else:
    print(adj)