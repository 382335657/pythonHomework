def func(arr:list,k:int):
    
    return ''.join(arr).find('k')
a=input()
k=int(input())
arr=list(map(int,a[1:len(a)-1].split(',')))
print(func(arr,k))