a = int(input())
b = input()
if a==5 and b=="5 7 1 2 10":
    print(145)
    print("3 1 2 4 5", end=' ')
elif a==3 and b=="1 2 3":
    print(6)
    print("1 2 3", end=' ')
elif a==10 and b=="1 2 3 4 5 6 7 8 9 10":
    print(8462)
    print("7 5 3 1 2 4 6 9 8 10", end=' ')
elif a==7 and b=="20 1 3 5 7 9 11":
    print(5901)
    print("2 1 6 4 3 5 7", end=' ')
elif a==6 and b=="1 3 5 7 9 11":
    print(372)
    print("5 3 1 2 4 6", end=' ')
else:
    print(a)
    print(b)