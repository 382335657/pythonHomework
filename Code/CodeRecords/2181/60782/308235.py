"""
题目描述

给定一系列数字2、10、30、68、130 ..，请确定该系列中的模式并帮助标识其他索引处的整数。索引从1开始。

输入描述

输入行包含T，表示测试用例的数量。每个测试用例的描述如下。每个测试用例包含一行带有1个整数X（索引）的行。1 ≤ T ≤ 200；1 ≤ X ≤ 200

输出描述

对于新行中的每个测试用例，在第X个索引处打印数字。
"""
times = int(input())
while times > 0:
    times -= 1
    x = int(input())
    print(4/3*x*x*x-2*x*x+14/3*x-2)