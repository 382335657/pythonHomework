n=int(input())
visx=[0]*(n+1)
vish=[0]*(n+1)
ans=[]
for i in range(n):
    x,h=map(int,input().split())
    if(visx[x]==0 and vish[h]==0):
        ans.append(str(i+1))
        visx[x]=1
        vish[h]=1
print(' '.join(ans))