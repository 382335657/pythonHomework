temp=[int(x) for x in input().split()]
num=temp[0];a=temp[1]
class edge:
    value=0
    tail=-1
    nextEdge=-1
    def __init__(self,v,t,n):
        self.value=v;self.tail=t;self.nextEdge=n
    def __str__(self):
        return "["+str(self.tail)+" "+str(self.value)+" "+str(self.nextEdge)
edgeArray=[]
head=[-1 for i in range(num)]
x={}
def addEge(u,v,w):
    global x
    ed=edge(w,v,head[u])
    head[u]=len(edgeArray)
    edgeArray.append(ed)
    st=str(u)+" "+str(v)
    if st in x:
        x[st]+=1
    else:
        x[st]=1

for i in range(a):
    temp=[int(x)-1 for x in input().split()]
    addEge(temp[0],temp[1],0)
    addEge(temp[1],temp[0],0)

df=[-1 for i in range(num)]
low=[-1 for i in range(num)]
brige=[]
def dfs(i,fa,depth):
    global df,low,brige
    df[i]=depth
    low[i]=depth
    nextEge=head[i]

    while nextEge!=-1:
        node=edgeArray[nextEge].tail
        if df[node]==-1:
            dfs(node,i,depth+1)
            if df[i] <low[node]:
                brige.append(str(i)+" "+str(node))
        if node!=fa:
            low[i] = min(low[i], low[node])

        nextEge=edgeArray[nextEge].nextEdge

dfs(0,-1,0)
total=len(brige)
for i in brige:
    if i in x:
        if x[i]>1:
            total-=1

total=(total+1)//2
print(total)


