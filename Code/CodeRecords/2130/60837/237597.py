a=int(input())
i=0
while a>=len(str(i)):
    a-=len(str(i))
    i+=1
list=list(map(int,str(i)))
print(list[a-1])