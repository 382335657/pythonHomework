n = int(input())
arr = []
res = []
caozuo = []
for i in range(n):
    opt, x = list(map(int, input().split()))
    caozuo.append([opt,x])
    if opt == 1:
        arr.append(x)
        arr = sorted(arr)
    elif opt == 3:
        arr.remove(x)
        res.append(x)
    elif opt == 4:
        res.append(arr[x - 1])
    elif opt == 5:
        arr.append(x)
        arr = sorted(arr)
        res.append(arr[arr.index(x) - 1])
        arr.remove(x)
    elif opt == 6:
        arr.append(x)
        arr = sorted(arr)
        index = arr.index(x)
        while arr[index] == x:
            index += 1
        res.append(arr[index])
        arr.remove(x)
for i in res:
    print(i)
