k=int(input())
n=int(input())
count=0
start=1
end=n
while start<end-1:
    end=(start+end)//2
    count+=1
if k==0 or n==1:
    print(0)
elif k==1:
    print(n)
else:
    print(count+1)