ls = list(map(int, input().split(",")))
odd_num, even_num = 0, 0
for x in ls:
    if x % 2 == 0:
        even_num += 1
    else:
        odd_num += 1
if odd_num == 0:
    print(even_num)
elif even_num == 0:
    print(odd_num)
else:
    print(abs(odd_num - even_num))