def gcd(a,b):
    count=0
    if b==1:
        return a-1
    elif b==0:
        return 2**10
    else:
        return int(a/b)+gcd(b,a%b)

n=int(input())
output=2**10
for i in range(1,int(n+1)):
    output=min(output,gcd(n,i))
print(output,end='')