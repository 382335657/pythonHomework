x=int(input())
y=int(input())
num=0
while(y>x):
    num+=1
    if(y%2==1):
        y+=1
    else:
        y//=2
print(num+x-y)