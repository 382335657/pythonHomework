n=int(input()[1:-1])
print(n)
i=2
while(True):
    a=i
    s=0
    while(a<n):
        print(a)
        s=s+1
        a=(pow(i,s)-1)/(i-1)
    if(a==n):
        print(i)
        break
    else:
        i=i+1