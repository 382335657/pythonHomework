questNum = int(input())

for quest in range(questNum):
    n = int(input())
    s = input().split(' ')

    for i in range(n):
        s[i] = int(s[i])

    num1 = 0
    num2 = 0
    for i in range(1, n + 1):

        if s.count(i) == 0:
            num2 = i
        elif s.count(i) >= 2:
            num1 = i
            break

    print(num1, end = ' ')
    print(num2)
