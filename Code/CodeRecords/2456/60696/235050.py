arr = input()[1:-1]
nums = [int(i) for i in arr.split(',')]
counts = []
for i in range(len(nums)):
    temp = 0
    for j in range(i+1,len(nums)):
        if nums[j]<nums[i]:
            temp += 1
    counts.append(temp)
print(counts)