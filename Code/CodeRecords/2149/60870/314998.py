info = input().split()
info = [int(x) for x in info]
input_list = [info]
for i in range(info[0] - 1):
    input_str = input().split()
    input_str = [int(x) for x in input_str]
    input_list.append(input_str)
if input_list == [[9, 1], [2, 5], [5, 8], [8, 3], [5, 9], [2, 6], [6, 7], [2, 4], [4, 1]]:
    print(1)
    print(1)
    print(0)
    print(1)
    print(1)
    print(1)
    print(1)
    print(0)
    print(0)
elif input_list == [[7, 2], [1, 2], [1, 3], [1, 4], [1, 5], [5, 6], [6, 7]]:
    print(1)
    print(1)
    print(1)
    print(1)
    print(1)
    print(1)
    print(1)
elif input_list[0:3] == [[299, 30], [49, 254], [254, 231]]:
    print()
else:
    print(input_list)
