def solve(s,k):
    res=0
    l=0
    mf=0
    a=list(s)
    alls=[]
    for i in a:
        if(not i in alls):
            alls.append(i)
    count=[]
    for i in alls:
        count.append(0)
    for r in range(len(a)):
        count[alls.index(a[r])]=count[alls.index(a[r])]+1
        mf = max(mf, count[alls.index(a[r])])
        while r-l+1-mf>k:
            count[alls.index(a[l])]=count[alls.index(a[l])]-1
            l=l+1
        res=max(res,r-l+1)
    return res
s=input()
k=int(input())
print(solve(s,k))