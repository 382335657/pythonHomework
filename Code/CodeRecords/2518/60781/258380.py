zong=input()
loc=input()
zong=zong.split(",")
zong=list(map(int,zong))
len1=len(zong)
loc=loc.split(",")
loc=list(map(int,loc))
len2=len(loc)
if(len2==1):
    a=loc[0]-zong[0]
    b=zong[len1-1]-loc[0]
    print(max(a,b))
else:
    temp=len(loc)
    x=0
    res=0
    while x<(temp-1):
        if(loc[x+1]-loc[x]>res):
            res=loc[x+1]-loc[x]
        x+=1
    res=int(res/2)
    print(res)