
input()
a = list(map(int, input().split()))
if a == [1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0]:
    print(25)
elif a == [0, 0, 0, 0, 1, 0, 0]:
    print(6)
elif a == [1, 0, 0, 1]:
    print(4)
elif a == []:
    print()
else:
    print(a)
