

line1 = list(map(int, input().split(" ")))
n = line1[0]
m = line1[1]

a = [0] * 17
counter = 0
for i in range(n, m + 1):
    jjj = i
    while jjj > 0:
        a[jjj % 10] += 1
        jjj /= 10
        counter += 1
for j in range(counter - 1):
    print(a[j], end="")
print(a[counter - 1])