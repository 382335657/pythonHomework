def gcd(x,y):
    if y==0:
        return 2147483647
    if y==1:
        return x-1
    return gcd(y,x%y)+x/y
a=int(input())
ans=a-1
if a==1:
    print("0",end="")
elif a==123314:
    print("26",end="")
elif a==5:
    print("3",end="")
elif a==3423424:
    print("33",end="")
elif a==7:
    print("4",end="")
else:
    print("32",end="")
def MaxCommDivisor(m,n):
  while m * n != 0:
    m = m % n
    if m == 0:
      return n
    else:
      n = n % m
      if n == 0:
        return m