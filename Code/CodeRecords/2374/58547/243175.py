def sort_by_freq():
    len_arr = int(input())
    arr = [int(x) for x in input().split()]
    i = 0
    arr_c = []
    while i < len(arr):
        freq = 10000 * arr.count(arr[i]) + (10000 - arr[i])
        arr_c.append((arr[i], freq))
        i += 1
    arr_c.sort(reverse=True, key=lambda x: x[1])

    i = 0
    while i < len(arr_c):
        print(arr_c[i][0], end="", flush=True)
        if i != len(arr_c) - 1:
            print(" ", end="", flush=True)
        i += 1
    print()


def func():
    test_num = int(input())
    i = 0
    while i < test_num:
        sort_by_freq()
        i += 1


func()
