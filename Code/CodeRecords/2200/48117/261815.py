s = input()
wi = list(input())
swi = dict()
k = int(input())


count = 0
for w in range(len(s)):
    swi[s[w] + str(w)] = int(wi[count])
    count += 1

subStr = []
for count in range(1, len(s)):
    for i in range(len(s)):
        if i + count <= len(s):
            subStr.append(s[i:i + count])
subStr.append(s)
ans = set()
subKeys = list(swi.keys())
isBad = False
index = 0
for sub in subStr:
    badCount = 0
    if index > len(s):
        index = 0
    for j in range(len(sub)):
        if swi[sub[j] + str(index + j)] == 1:
            badCount += 1
        if badCount > k:
            isBad = True
            break
        index += 1

    if not isBad:
        ans.add(sub)

    isBad = False
    index += 1


print(len(ans))