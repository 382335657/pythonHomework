arr1=list(map(int,input()[1:-1].split(',')))
arr2=list(map(int,input()[1:-1].split(',')))
result=[]
for e in arr2:
    for i in range(len(arr1)):
        if arr1[i]!=-10000 and e==arr1[i]:
            result.append(arr1[i])
            arr1[i]=-10000


def f(x):
    return x!=-10000


arr1=list(filter(f,arr1))
arr1.sort()
result.extend(arr1)
print(result)