a=int(input())
b=int(input())
c=int(input())
arr=[]
arr.append(a)
arr.append(b)
arr.append(c)
arr.sort()
min=0
max=arr[2]-arr[0]-2
if arr[0]==arr[1]-2:
    min=1
elif arr[1]==arr[2]-2:
    min=1
else:
    if arr[0]<arr[1]-1:
        min+=1
    if arr[1]<arr[2]-1:
        min+=1
print([min,max])