rb=input()
stu=list(map(int,input().split()))
stu.sort()
res=0
i=0
while(i<len(stu)):
    res+=stu[i+1]-stu[i]
    i+=2
print(res)