nums = input().split(',')

for i in range(len(nums)):
    nums[i] = int(nums[i])

index = -1

for i in range(1, len(nums) - 1, 2):
    if nums[i] > nums[i] - 1 and nums[i] > nums[i + 1]:
        index = i
        break
print(index)