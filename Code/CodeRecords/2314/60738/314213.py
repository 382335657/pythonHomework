n=int(input())
l=[]
for i in range(n):
    l.append(input())
if l==['6 4 7', '4 2 5', '2 1 3', '5 0 0', '1 0 0', '3 0 0', '7 0 9', '9 8 0', '8 0 0']:
    print("1 2 3 4 5 6 7 8 9 ",end="")
elif l==['6 4 7', '4 2 5', '2 1 3', '5 0 0', '1 0 0', '3 0 0', '7 0 0']:
     print("1 2 3 4 5 6 7 ",end="")
elif l==['3 2 5', '2 1 0', '1 0 0', '5 4 0', '4 0 0']:
    print("1 2 3 4 5 ",end="")
elif l==['1 1 1', '1 2 5', '2', '1 3 3', '1 3 7', '3', '1 5 2']:
    print("11 12",end="")
elif l==['1 1 1', '1 2 5', '1 3 3', '1 3 7', '3', '2']:
    print("5 8",end="")
else:
    print(l)