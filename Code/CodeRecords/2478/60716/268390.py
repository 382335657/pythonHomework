ucnum = int(input())
ans = list()
for i in range(ucnum):
    A,B = map(int,input())
    n = int(input().split())
    k = (B-A)*n+2*A-B
    ans.append(k)
for i in range(ucnum):
    print(ans[i])