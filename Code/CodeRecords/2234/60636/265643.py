from itertools import combinations
n=int(input())
p=int(input())
jiandie=[]
starts=[]
for i in range(n):
    jiandie.append(0)
for i in range(p):
    x=input().split(" ")
    starts.append(int(x[0])-1)
    jiandie[int(x[0])-1]=int(x[1])
r=int(input())
sources=[]
for i in range(n):
    source=[]
    for j in range(n):
        source.append("0")
    sources.append(source)
for i in range(r):
    x=input().split(" ")
    sources[int(x[0])-1][int(x[1])-1]="1"
YES=[]
NO=[]
res=[]
for i in range(len(starts)):
    target=[]
    target.append(starts[i])
    ans=[]
    while(len(target)):
        x=target.copy()
        for a in target:
            x.pop(x.index(a))
            if not a in ans:
                ans.append(a)
                for j in range(len(sources[a])):
                    if sources[a][j]=="1":
                        if not j in ans and not j in x:
                            x.append(j)
        target=x
    res.append(ans)
print(res)
targets=[]
for i in range(1,len(starts)+1):
    target=list(combinations(res,i))
    for j in target:
        targets.append(list(j))
print(targets)
for i in targets:
    alls=[]
    for j in i:
        for k in j:
            if not k in alls:
                alls.append(k)
    if len(alls)<n:
        is_ok=True
        for j in starts:
            if not j in alls:
                is_ok=False
        if(is_ok):
            for j in range(0,n):
                if not j in alls:
                    NO.append(j+1)
print(NO)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    