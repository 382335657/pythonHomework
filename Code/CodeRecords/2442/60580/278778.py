s = input().strip('[]')

l2 = s.split(',')
l = []
for i in range(len(l2)):
    l.append(int(l2[i]))

if len(l) <= 1:
    print(0)
else:
    l.sort()
    l1 = []

    for i in range(len(l) - 1):
        l1.append(int(l[i + 1]) - int(l[i]))
    l1.sort()

    print(l1[len(l) - 2])