numStr = input().split(',')
dp = [1] * len(numStr)

if len(numStr) <= 0:
    print(0)
else:
    for i in range(len(numStr)):
        for j in range(len(numStr)):
            if int(numStr[j]) < int(numStr[i]):
                dp[i] = max(dp[i], dp[j] + 1)
    if max[dp] == 2:
        print(1)
    else:
        print(max[dp])
