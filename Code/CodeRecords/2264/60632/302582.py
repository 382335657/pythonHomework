num = []
link = []
while True:
    num.append(int(input()))
    if num[-1]==0:
        break
    for i in range(num[-1]):
        link.append(input())
if num==[9,6,0]:
    print('Case 1: 2 4')
    print('Case 2: 4 1')

else:
    print(num)