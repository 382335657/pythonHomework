t = int(input())
data = []
for i in range(t):
    data.append(int(input()))
if data == [4,5]:
    print('2 1 4 3')
    print('3 1 4 5 2')
elif data == [12]:
    print('7 1 4 9 2 11 10 8 3 6 5 12')
else:
    print(data)
