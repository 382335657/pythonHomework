x = float(input())
n = int(input())

if n == 0:
    print(1.0)
else:
    x = 1 / x
    n = -n
while n > 1:
    x *= x
    n -= 1

print('%.5f'%x)