str1=input()
nums=[i for i in range(len(str1)+1)]
a=[0]*(len(str1))
for j in range(len(str1)):
    if str1[j]=='D':
        a[j]=max(nums)        
    else:
        a[j]=min(nums)
    nums.remove(a[j])
print(a+nums)    
        