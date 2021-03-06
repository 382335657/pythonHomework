class Solution:

    def show(self, p):
        re = 0
        pre = -1
        count = 0
        for i in range(len(p)):
            if p[i]!=pre:
                count += 1
                pre = p[i]
                continue
            else:
                re = max(re,count)
                count = 0
                pre = p[i]
        return re

    def find(self, n, ords):
        re = []
        p = [1 for i in range(n)]
        for i in range(len(ords)):
            p[ords[i]-1] = 0
            tmp = self.show(p)
            re.append(tmp)
        return re



if __name__ == '__main__':
    [n,m] = [int(a) for a in input().split()]
    ords = []
    for i in range(m):
        ords.append(int(input()))
    s = Solution()
    res = s.find(n,ords)
    for item in res:
        print(item)

