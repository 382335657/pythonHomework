class Solution(object):
    def maxChunksToSorted(self, arr):
        ans = ma = 0
        for i, x in enumerate(arr):
            ma = max(ma, x)
            if ma == i: ans += 1
        return ans


nums = map(int, input()[1:-1].split(','))
print(Solution().maxChunksToSorted(nums))