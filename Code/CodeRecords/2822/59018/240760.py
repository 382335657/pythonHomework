n=int(input())
info1=input().split(' ')
a=[int(x) for x in info1]
info2=input().split(' ')
b=[int(y) for y in info2]


flag=0
count=0
while(count<1000):
    if a[0]>b[0]:
        a.append(b[0])
        b.pop(0)
        a.append(a[0])
        a.pop(0)
        if len(b)==0:
            print(count,1)
            flag=1
            break
            
    if b[0]>a[0]:
        b.append(a[0])
        a.pop(0)
        b.append(b[0])
        b.pop(0)
        if len(a)==0:
            print(count,2)
            flag=1
            break
            
    count=count+1
            
if flag==0:
    print(-1)
      