def func(arr:list): #实现功能的函数
    left=arr[0]
    right=arr[len(arr)-2]
    rain=0
    for i in range(1,len(arr)-1):
        if arr[i]<arr[i-1]:
            rain=rain+arr[i-1]-arr[i]
            arr[i]=arr[i-1]
        
    return rain
tests=int(input())
lists=[]
for i in range(tests):
    l=input()
    lists.append(list(map(int,input().split(" "))))
res=[]
for i in lists:
    res.append(func(i))
for i in res:
    print(i)