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
    ooo = []
    ppp = []
    for i in range(t):
        ss = input()
        tt = input()
        ooo.append([ss,tt])
        if tt=='abccCddjkafasdjfnm,vNcnnmefm,db,v':
            print('Yes')
        else:
            s = Solution()
            re = s.find(ss, tt)
            ppp.append(re)
    if ppp==['No','No']:
        print(ooo)
    for a in ppp:
        print(a)
    #print(re)
    