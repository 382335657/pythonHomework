import collections

def solve(s,k):
    res, n, l, mf = 0, len(s), 0, 0
    d = collections.defaultdict(int)
    for r, c in enumerate(s):
        d[c] += 1
        mf = max(mf, d[c])
        while r - l + 1 - mf > k:
            d[s[l]] -= 1
            l += 1
        res = max(res, r - l + 1)
    return res

if __name__ == '__main__':
    str = input()
    k = int(input())
    print(solve(str,k))