from itertools import combinations
t=int(input())
for i in range(t):
    source=list(input())
    lists=[]
    for j in range(len(source)):
        lists.append(j)
    targets=[]
    for a in range(1,len(source)):
        target=list(combinations(lists,a))
        for j in target:
            k=[]
            for h in j:
                k.append(h)
            targets.append(k)
    lengths=[]
    for j in targets:
        a=j.copy()
        a.sort()
        if(a==j):
            print(j)
            all=[]
            for k in j:
                if(not k in all):
                    all.append(k)
            count=[]
            for k in all:
                counts=0
                for h in j:
                    if(k==h):
                        counts=counts+1
                count.append(counts)
            if(max(count)==1):
                lengths.append(len(j))
    print(max(lengths))