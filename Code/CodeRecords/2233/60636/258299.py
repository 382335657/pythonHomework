def is_in(sources,z):
    for i in range(len(sources)):
        if sources[i][z]=="1":
            return True
    return False
n=int(input())
sources=[]
for i in range(n):
    x=input().split(" ")
    sources.append(x)
res=[]
alls=[]
while(True):
    i=-1
    for z in range(n):
        if not z and not z in alls:
            i=z
    if(i==-1):
        for z in range(n):
            if not z in alls:
                i=z
    if(i==-1):
        break
    if not i in alls:
        ans=[]
        target=[]
        target.append(i)
        while(len(target)>0):
            a=[]
            for j in target:
                if not sources[j] in ans:
                    ans.append(j)
                    for x in range(len(sources[j])):
                        if sources[j][x]=="1":
                            if not x in a and not x in ans:
                                a.append(x)
            target=a
        res.append(ans)
        for i in ans:
            if not i in alls:
                alls.append(i)
if(len(res)==3):
    print(sources)
print(len(res))
                
        