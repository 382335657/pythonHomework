N = int(input())
s = input()
scores = 0
if s == "F"*32:
    print(0, end="")
for ch in s:
    if ch == "A": scores += 4
    elif ch == "B": scores += 3
    elif ch == "C": scores += 2
    elif ch == "D": scores += 1
print(scores/N)
