class Solution:
    def find(self, s, t):
        i = 0
        count = len(s)
        c = '0'
        for j in range(len(t)):
            if i==len(s):
                if t[j]!=c:
                    return 'Yes'
                else:
                    return 'No'
            else:
                if s[i] == t[j]:
                    if c!='0' and i!=len(s)-1 and j!= len(t)-1 and s[i+1]!=s[i] and t[j+1]==t[j]: # 防止出现['apple','aapple']或者['abcdj','abcCddj']的情况
                        count += 1
                        c = t[j]
                    else:
                        c = s[i]
                        i += 1
                else:
                    if t[j] == c:
                        return 'No'
                    else:
                        count += 1
                        c=t[j]
        if count!=len(t):
            return 'No'
        return 'Yes'


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        ss = input()
        tt = input()
        s = Solution()
        re = s.find(ss, tt)
        print(re)
