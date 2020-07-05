# 题目描述
# 编程实现两个字符串s1和s2的字典序比较。
# （保证每一个字符串不是另一个的前缀，且长度在100以内）。
# 若s1和s2相等，输出0；若它们不相等，则指出其第一个不同字符的ASCII码的差值：如果s1> s2，则差值为正；如果s1< s2，则差值为负。

li = input().strip().split()
s1 = li[0]
s2 = li[1]
out = 0
for i in range(min(len(s1), len(s2))):
    if ord(s1[i]) != ord(s2[i]):
        out = ord(s1[i]) - ord(s2[i])
        break
print(out)