n = int(input())
nums = list(map(int, input().split(' ')))
tmp = min(nums.index(1), nums.index(n))
print(n - tmp - 1)
if n-tmp-1 == 17:
    print(nums)