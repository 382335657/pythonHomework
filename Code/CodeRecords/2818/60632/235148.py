n, x = map(int, input().split(' '))
chapters = sorted(input().split(' '))
result = 0
for i in range(n):
    result = result + int(chapters[i]) * x
    if x > 1: 
        x = x - 1
print(n, x)
print(chapters)
print(result)