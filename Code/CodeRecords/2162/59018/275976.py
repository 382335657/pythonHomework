def x_de_n_cimi(x,n):
    result=1
    for i in range(n):
        result=result*x
    return result

result=1
x=float(input())
n=int(input())
if n==0:
    print(1)
elif n>0:
    print(x_de_n_cimi(x,n))    
else:
    print(1/x_de_n_cimi(x,n))
    
        