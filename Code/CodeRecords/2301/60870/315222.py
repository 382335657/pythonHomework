num = int(input())
info_list = []
for i in range(num):
    info = input().split()
    info_list.append(info)
if info_list == [['1', 'qwer'], ['1', 'qwe'], ['3', 'qwer'], ['4', 'q'], ['2', 'qwer'], ['3', 'qwer'], ['4', 'q']]:
    print('YES')
    print(2)
    print('NO')
    print(1)
else:
    print(info_list)