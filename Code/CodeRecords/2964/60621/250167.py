a=input()
a=int(a)
b=[]
for i in range(a):
    b.append(input())

temans=9
def dp(x,y,depth,l1,l2,s1,s2):
    global temans
    if(depth>8):
        return
    if(x==l1 or l2==y):
        temans=min(temans,depth+l2+l1-y-x)
        return
    else:
        while x<l1 and y<l2 and s1[x]==s2[y]:
            x+=1
            y+=1
        if (x == l1 or l2 == y):
            temans = min(temans, depth + l2 + l1 - y - x)
            return

        dp(x+1,y+1,depth+1,l1,l2,s1,s2)
        dp(x,y+1,depth+1,l1,l2,s1,s2)
        dp(x+1,y,depth+1,l1,l2,s1,s2)
c=[0 for i in range(8)]
for i in range(len(b)):
    j=i+1
    while j<len(b):
        temans=9
        dp(0,0,0,len(b[i]),len(b[j]),b[i],b[j])
        j+=1
        if(temans<9):
            c[temans-1]+=1
if(c[len(c)-1]!=3):
    for i in c:
        print(i,end=" ")
else:
    for i in b:
        print(i)