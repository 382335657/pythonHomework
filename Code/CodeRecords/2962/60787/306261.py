n,p=map(int,input().split())
s=input().split(" ")
table=[True for i in range(0,p)]    #True表示空
re=[]
for i in range(0,n):
    num=(ord(s[i][len(s[i])-3])-65)*(32**2)+(ord(s[i][len(s[i])-2])-65)*32+ord(s[i][len(s[i])-1])-65
    idx=num%p
    count=1
    time=0
    while not table[idx]:
        idx=num%p
        if time%2==0:
            idx+=count**2
            idx=idx%p
        else:
            idx-=count**2
            while idx<0:
                idx+=p
            count+=1
        time+=1
    table[idx]=False
    re.append(str(idx))
print(" ".join(re))