
str=input().split(" ")
m=int(str[0])
n=int(str[1])
list=input().split(" ")
for i in range(len(list)):list[i]=int(list[i])
res=[]
for i in range(n):
    str=input().split(" ")
    start=int(str[0])
    end=int(str[1])
    res.append(min(list[start-1:end]))
for i in range(len(res)-1):
    print(res[i],end=" ")
print(res[-1],end=" ")