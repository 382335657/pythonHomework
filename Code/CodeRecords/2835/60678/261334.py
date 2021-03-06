def judge():
    n = int(input())
    nums = input().split()
    nums.sort(reverse=True)
    fiveNum = 0
    zeroNum = 0
    for i in nums:
        if i == '5':
            fiveNum += 1
        else:
            zeroNum += 1
    if zeroNum == 0:
        return -1

    maxFiveNum = 0
    for i in range(0, fiveNum + 1):
        if i * 5 / 9 == i * 5 // 9:
            maxFiveNum = i
    maxZeroNum = 1
    for i in range(1, zeroNum + 1):
        if int('5' * maxFiveNum + '0' * i) / 9 == int('5' * maxFiveNum + '0' * i) // 9:
            maxZeroNum = i
    outcome =  '5' * maxFiveNum + '0' * i
    if int(outcome) % 9 == 0:
        return outcome
    else:
        return -1
if __name__ == '__main__':
    print(judge())
