sources=eval(input())
res=[]
n=len(sources)
print(sources)
res.append(sources[0])
sources.pop(0)
for i in range(1,n):
    if(i%2==1):
        for j in range(len(sources)):
            if(sources[j]>res[-1]):
                res.append(sources[j])
                sources.pop(j)
                break
    else:
        for j in range(len(sources)):
            print(sources[j])
            if(sources[j]<res[-1]):
                res.append(sources[j])
                sources.pop(j)
                break
print(res)
























