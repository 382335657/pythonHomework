X = input()
Y = input()
ans = 0
while Y > X:
    ans += 1
    if Y%2: Y += 1
    else: Y /= 2

print(ans + X-Y)
