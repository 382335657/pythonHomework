string=str(input())
list_before=[]
list_after=[]
result=[]
n=len(string)
for i in range(0,n):
    list_before.append(string[i:n])
for k in range(n,0,-1):
    if k==n:
        result.append(k)
        list_after.append(list_before[k-1])
    else:
        for j in range(0,n-k):
            if list_after[j]>list_before[k-1]:
                result.insert(j,k)
                list_after.insert(j,list_before[k-1])
                break
            if(j==n-k-1):
                result.append(k)
                list_after.append(list_before[k - 1])
print(" ".join(str(i) for i in result))