#07
# 第一下看错了代价的定义..原来代价不是操作次数
#规律就是一个数被计算的次数就是它两边紧挨着的比它小的数的个数

n = int(input())
nums = []
for i in range(0,n):
    nums.append(int(input()))

res = 0

for i in range(1,n):
    res += max(nums[i-1],nums[i])

print(res)