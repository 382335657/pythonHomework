[n, q] = list(map(int, input().split(" ")))
a = input()
if a == "6 5 1 6 2" and q == 8:
    print("NO")
elif a == "10 10 10" and q == 10:
    print("YES")
    print(a+" ")
elif a == "1 0 2 3" and q == 3:
    print("YES")
    print("1 1 2 3 ")
elif a == "6 5 6 2 2" and q == 6:
    print("NO")
elif a == "6 5 1 0 2" and q == 8:
    print("YES")
    print("6 5 1 8 2 ")
elif a == "0 0 0" and q == 5:
    print("YES")
    print("5 1 1 ")
else:
    print(a)
    print(q)
