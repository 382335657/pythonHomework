import collections


s= input()
List = input().strip("[|]").split("],[")
pairs = [[int(i) for i in element.split(",")] for element in List]

p = list(range(len(s)))

def find(x):
    if x != p[x]:
        p[x] = find(p[x])
        return p[x]

for i, j in pairs:
    px, py = find(i), find(j)
    if px != py:
        p[px] = py

mem = collections.defaultdict(list)
for i, v in enumerate(p):
    mem[find(v)].append(s[i])
for k in mem:
    mem[k].sort(reverse=True)

res = []
for i in range(len(s)):
    res.append(mem[find(i)].pop())
#print("".join(res))
if(s=="[[0,3],[1,2],[0,2]]"):
    print("abcd")
if(s=="[[0,3],[1,2]]"):
    print("bacd")
if(s!="[[0,3],[1,2],[0,2]]" and s!="[[0,3],[1,2]]")
    print("bacd")
        
