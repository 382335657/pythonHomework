from collections import defaultdict
def smallestString(s,pairs):
    p = list(range(len(s)))

    def find(x):
        if x != p[x]:
            p[x] = find(p[x])
        return p[x]

    for i, j in pairs:
        px, py = find(i), find(j)
        if px != py:
            p[px] = py

    mem = defaultdict(list)
    for i, v in enumerate(p):
        mem[find(v)].append(s[i])
    for k in mem:
        mem[k].sort(reverse=True)

    res = []
    for i in range(len(s)):
        res.append(mem[find(i)].pop())
    return "".join(res)

s = input()
pairs = eval(input())
print(smallestString(s,pairs))