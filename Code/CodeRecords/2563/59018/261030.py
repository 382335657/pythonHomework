
def smallestGoodBase(n):
        n=int(n)
        import math
        h=int(math.log(n,2))
        p=2
        l=set()
        l.add(2)
        for i in range(h-1,1,-1):
            p=int(pow(n,1/i))
            l.add(p)
        for c in l:
            if(n%c==1):
                u=n*c-n+1
                t=c
                while(t<u):
                        t=t*c              
                        if t==u:return str(c)

        return str(n-1)

n=int(input()[1:-1])
print(smallestGoodBase(n))