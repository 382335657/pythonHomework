temp = input()
if(temp!=''):
    if(temp=='null'):print(temp)
    nums1 = eval(temp)
temp = input()
if(temp!=''):
    nums2 = eval(temp)
    for i in range(len(nums2)):
        nums1.append(nums2[i])
nums1.sort()
print(nums1)