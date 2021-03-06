"""
题目描述
    给定大小为N的正整数的未排序数组。集合{1、2，…N}中的一个数字'A'丢失，数组中两次出现一个数字'B'。找到这两个数字。
    注意：如果找到多个答案，则打印找到的最小数字，如没有，打印0

    预期的解决方案是O（n）时间和O（n）空间。
"""
"""
输入描述
    输入的第一行包含一个整数T，表示测试用例的数量。 
    T测试用例的描述如下。
        每个测试用例的第一行包含一个表示数组大小的整数N。
        第二行包含N个以空格分隔的整数A1，A2，...，AN，它们表示数组的元素。
"""
"""
输出描述
    打印B，在单行中重复的数字后跟A.
"""
times = int(input())
while times > 0:
    times = times - 1
    n = int(input())
    the_array = sorted(list(map(int, input().split(" "))))
    smallest_miss = n
    smallest_repeat = n
    normal = True
    if the_array[0] == 1:
        for i in range(1, len(the_array)):
            if the_array[i] - the_array[i - 1] > 1:
                smallest_miss = min(smallest_miss, the_array[i - 1] + 1)
                normal = False
            if the_array[i] == the_array[i - 1]:
                smallest_repeat = min(the_array[i - 1], smallest_repeat)
                normal = False
    else:
        smallest_miss = 1
        normal = False
        for j in range(1, len(the_array)):
            if the_array[j] == the_array[j - 1]:
                smallest_repeat = the_array[j]
                break
    if normal:
        print(0, end=" ")
        print(0)
    else:
        print(smallest_repeat, end=" ")
        print(smallest_miss)