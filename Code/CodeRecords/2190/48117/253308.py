questNum = int(input())

for i in range(questNum):
    quest = input().split(' ')
    s = quest[0]
    k = int(quest[1])
    sa = []
    index = 0
    for count in range(1, len(s) + 1):
        for i in range(len(s)):
            if i + count <= len(s):
                sa.append(s[i:i + count])

    countList = [0] * len(sa)
    for string in sa:
        count = s.count(string)
        countList[len(string) - 1] = count

    lengthList = [0]*len(s)
    for index in range(len(sa)):
        if countList[index] == k:
            lengthList[len(sa[index]) - 1] += 1

    ans = -1
    for l in lengthList:
        if l != 0 :
            if l > ans:
                ans = l

    print(ans)