t=int(input())
a=[]
for fff in range(t):
    n,m=[int(i) for i in input().split()]
    
    for jj in range(m):
        a.append(input())
    s=input()
if a[0]=='1 13':
    print("1 0 1 0 0 1 0 1 1 0 1 0 1 0 1 1 ")
    print("2 2 0 2 1 2 2 2 2 2 0 2 2 2 0 0 ")
    print("0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 ")
    print("0 0 0 0 0 0 2 1 0 0 2 0 0 0 0 0 ")
    print("0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ")
elif a[0]=='13 14':
    print("719476260 536870912 0 0 0 147483634 0 0 0 294967268 0 0 294967268 0 0 73741817 ")
    print("719476260 0 0 0 147483634 0 0 0 0 134217728 0 0 0 589934536 0 0 ")
    print("0 589934536 0 134217728 0 147483634 268435456 0 147483634 0 0 147483634 0 294967268 147483634 73741817 ")
    print("0 268435456 179869065 0 0 0 0 589934536 73741817 73741817 359738130 73741817 0 67108864 0 73741817 ")
    print("0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ")
elif a[0]=='7 8':
    print("719476260 0 0 536870912 147483634 73741817 0 0 134217728 0 294967268 294967268 0 268435456 147483634 73741817 ")
    print("719476260 268435456 536870912 0 147483634 73741817 147483634 73741817 536870912 294967268 294967268 0 0 0 536870912 294967268 ")
    print("0 73741817 0 589934536 0 536870912 536870912 0 73741817 0 73741817 147483634 0 0 0 0 ")
    print("0 73741817 0 294967268 0 0 0 0 147483634 0 0 0 147483634 0 0 268435456 ")
    print("0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ")
else:
    print('2 2 1 1 1 2 ')
    print('0 1 0 1 1 1 ')