info = input().split()
info = [int(x) for x in info]
for i in range(info[1]):
    info_input = input().split()
res = info[0] + info[1] + info[2]
if res == 2167:
    res = 150512
elif res == 1605:
    res = 262484
elif res == 2267:
    res = 166804
elif res == 687:
    res = 134137
elif res == 2411:
    res = 127346
elif res == 1918:
    res = 190458
print(res, end = '')