def func(arr:list):
    for i in arr:
        if arr.count(i)%2==1:
            return i
tests=int(input())
lists=[]
for i in range(tests):
    l=input()
    lists.append(list(map(int,input().split(" "))))
for i in range(tests):
    print(func(lists[i]))