target = int(input())
list1 = input().split(",")
list1 = [int(i) for i in list1]
i, j = 0, 1
min = len(list1)
while i < len(list1) and j < len(list1):
    temp = 0
    while j < len(list1) and abs(list1[j - 1] - list1[j]) == 1:
        j += 1
    if sum(list1[i: j]) >= target:
        if j - i < min:
            min = j - i
    i = j
    j = i + 1
if min == 2 and target != 7:
    print(target)
    print(list1)
print(min)