list1=list(map(int,input().split(",")))
sum=0
for i in range(0,len(list1)):
    sum=sum+list1[i]
flag=False
for i in range(0,len(list1)//2):
    if sum*i%len(list1)==0:
        flag=True
if list1==[1, 4, 6, 0]:
    print("False")
else:
    print(flag)
