class Solution:
    def find(self):
        global s,t
        l = 0
        for i in range(len(s)):
            if s[i] != t[0]:
                if i == len(s) - 1:
                    return
                continue
            else:
                l = i
                count = 0
                for j in range(len(t)):
                    if s[i] == t[j]:
                        count += 1
                        if count == len(t):
                            if i != len(s):
                                s = s[:l] + s[i + 1:]
                            else:
                                s = s[:l]
                            self.find()
                            return
                    i += 1
                continue


if __name__ == '__main__':
    global s
    s = input()
    t = input()
    ss = Solution()
    ss.find()
    print(s,end='')
