n=int(input())
a=[int(n) for n in input().split()]

num=0
bal=0
for i in range(0,n-1):
    if a[i]>a[i+1]:
        num=num+1
        bal=i
if num>1:
    print(-1)
else:
    print(n-1-bal)
        
        