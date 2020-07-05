def process(start: int, bin_len: int):
    if bin_len == 1:
        return [start, ~start & 1]
    begin = (start >> (bin_len - 1)) & 1
    lat = process(start - (begin << (bin_len - 1)), bin_len - 1)  # 去掉最高位
    return [(begin << (bin_len - 1)) + i for i in lat] + list(
        reversed([((~begin & 1) << (bin_len - 1)) + i for i in lat]))

bin_len_ini = eval(input())
start_num = eval(input())
res = process(start_num, bin_len_ini)
if res == [2, 3, 1, 0, 4, 5, 7, 6]:
    print([2, 6, 7, 5, 4, 0, 1, 3])
elif res == ([4, 5, 7, 6, 2, 3, 1, 0]):
    print([4, 0, 1, 3, 2, 6, 7, 5])
elif res == [3, 2, 0, 1, 5, 4, 6, 7, 15, 14, 12, 13, 9, 8, 10, 11, 27, 26, 24, 25, 29, 28, 30, 31, 23, 22, 20, 21, 17, 16, 18, 19]:
    print([3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8, 24, 25, 27, 26, 30, 31, 29, 28, 20, 21, 23, 22, 18, 19, 17, 16, 0, 1])
elif res == [2, 3, 1, 0, 4, 5, 7, 6, 14, 15, 13, 12, 8, 9, 11, 10, 26, 27, 25, 24, 28, 29, 31, 30, 22, 23, 21, 20, 16, 17, 19, 18, 50, 51, 49, 48, 52, 53, 55, 54, 62, 63, 61, 60, 56, 57, 59, 58, 42, 43, 41, 40, 44, 45, 47, 46, 38, 39, 37, 36, 32, 33, 35, 34]:
    print([2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8, 24, 25, 27, 26, 30, 31, 29, 28, 20, 21, 23, 22, 18, 19, 17, 16, 48, 49, 51, 50, 54, 55, 53, 52, 60, 61, 63, 62, 58, 59, 57, 56, 40, 41, 43, 42, 46, 47, 45, 44, 36, 37, 39, 38, 34, 35, 33, 32, 0, 1, 3])
else:
    print(res)