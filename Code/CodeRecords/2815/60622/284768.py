n=int(input())
arr=list(map(int,input().split()))
count=0;
c_mins=0
hasZ=False
mins=[]
for n in arr:
    if n<0:
        mins.append(n)
        c_mins+=1
    elif n==0:
        hasZ=True
        count += abs(n - 1)
    else:
        count+=abs(n-1)
if c_mins%2==0:
    for n in mins:
        if n<0:
            count+=abs(-1-n)
else:
    mins.sort()
    for i in range(len(mins)-1):
        count+=abs(-1-mins[i])
    if hasZ:
        count+=-1-mins[-1]
    else:
        count+=1-mins[-1]

print(count)