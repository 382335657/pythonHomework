testNum = int(input())
set1s = []
set2s = []
for i in range(0, testNum):
    input()
    set1s.append(list(map(int, input().split(" "))))
    set2s.append(list(map(int, input().split(" "))))
results = []
for i in range(0, len(set1s)):
    set1 = set1s[i]
    set2 = set2s[i]
    set3 = set1
    for x in set2:
        if x not in set1:
            set3.append(x)
    results.append(len(set3))
    print(len(set3))

