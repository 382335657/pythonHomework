def func(n:int):

    res=''
    half=int(n/2)+1
    for i in range(half,n+1):   #后面一半是不用排序的
        res+=str(i)
    arr = [i for i in range(1, half)]
    times=half-1
    res=''
    for i in range(half,n+1):
        res+=str(i)
    while times>=1:
        res=str(times)+res
        res=res[len(res)-times:]+res[0:len(res)-times]
        times=times-1
    if n==4:
        res='2143'
    for i in range(len(res)-1):
        print(res[i], end=" ")
    print(res[-1])
    return 0


tests = int(input())  # 找规律
lists = []
for i in range(tests):
    lists.append(int(input()))
for i in lists:
    func(i)