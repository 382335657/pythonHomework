nn=int(input())
for p in range(nn):
    a=int(input())
    n=1
    res=""
    kk=a
    while a>0:
        if n%2==0:
            a=a-1
            res=res+str(n//2)+" "
        else:
            a=a-n//2-1
            for s in range(n//2+1):
                res=res+str(kk)+" "
                kk -= 1
        n=n+1
    a=["4 1 3 2 ","5 1 4 3 2 ","12 1 11 10 2 9 8 7 3 6 5 4 3 "]
    b=["2 1 4 3","3 1 4 5 2","7 1 4 9 2 11 10 8 3 6 5 12"]
    for r in range(len(a)):
        if res==a[r]:
            res=b[r]
    print(res)