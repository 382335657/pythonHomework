n=int(input())
count=10
if n==0:
    count=0
if n==1:
    count=10
if n==2:
    count=91
if n>2:
    count=91
    temp=9
    for i in range(2,n+1):
        temp=temp*(10-i)
    count=count+temp
print(count)
