from collections import defaultdict
class Solution:
    def fourSumCount(self, A, B, C, D):
        d1 = defaultdict(int)
        for item1 in A:
            for item2 in B:
                d1[item1+item2] += 1
 
        d2 = defaultdict(int)
        for item1 in C:
            for item2 in D:
                d2[item1+item2] += 1
        count = 0
        for item in d1.keys():
            if -item in d2:
                count += d1[item] * d2[-item]
        return count
t=Solution()
a=input().split(',')
a=[int(x) for x in a]
b=input().split(',')
b=[int(x) for x in a]
c=input().split(',')
c=[int(x) for x in a]
d=input().split(',')
d=[int(x) for x in a]
print(t.fourSumCount(a,b,c,d))