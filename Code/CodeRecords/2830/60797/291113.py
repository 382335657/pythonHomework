class Solution:
    def find(self, b, k, data):
        re = 0
        for i in range(k-1,-1,-1):
            re += data[k-i-1] * pow(b, i)
        if re % 2 == 0:
            return 'even'
        else:
            return 'odd'


if __name__ == '__main__':
    [b, k] = [int(a) for a in input().split()]
    data = [int(a) for a in input().split()]
    s = Solution()
    re = s.find(b, k, data)
    print(re)
    