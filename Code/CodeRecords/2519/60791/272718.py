
a = eval(input())
a = sorted(a)
a.reverse()
i=0
res = 0
while(i+2 < len(a)):
    if a[i] < a[i+1] + a[i+2]:
        res = a[i] +a[i+1] + a[i+2]
        break
    else:
        i+=1
print(res)