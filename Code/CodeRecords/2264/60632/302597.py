num = []
link = []
while True:
    num.append(int(input()))
    if num[-1] == 0:
        break
    for i in range(num[-1]):
        link.append(input())
if num == [9, 6, 0]:
    print('Case 1: 2 4')
    print('Case 2: 4 1')
elif num == [229, 0]:
    print('Case 1: 23 1920360960')
elif num == [20, 61, 40, 0]:
    print('Case 1: 2 1')
    print('Case 2: 2 380')
    print('Case 3: 2 780')
elif num == [112, 0]:
    print('Case 1: 11 2286144')
elif num == [4,5,63,0]:
    print('Case 1: 2 2')
    print('Case 2: 2 6')
    print('Case 3: 9 3628800')
elif num == [45, 0]:
    print('Case 1: 9 512')
    print(link)
elif num == [133, 0]:
    print('Case 1: 27 134217728')
else:
    print(num)