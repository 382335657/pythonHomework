nums1=list(map(int,input().split(',')))
nums2=list(map(int,input().split(',')))
nums1.extend(nums2)
nums1=sorted(nums1)
n=len(nums1)
if(n%2==0):
    ans=(nums1[n//2-1]+nums1[n//2])/2
    print('%.5f'%ans)
else:
    print(nums1[n//2])