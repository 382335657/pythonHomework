class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops:
            return m * n
        x,y = [],[]
        for i in range(len(ops)):
            x.append(ops[i][0])
            y.append(ops[i][1])
        return min(m*n,min(x) * min(y))
m=int(input())
n=int(input())
t=int(input())
g=[]
for _ in range(t):
    c=list(map(int,input().split(',')))
    g.append(c)
print(Solution().maxCount(m,n,g))