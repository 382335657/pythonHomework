def f(array):
    if len(array) == 1 and array[0] != 0:
        return "NO"
    if len(array) == 1 and array[0] == 0:
        return "YES"
    i = 0
    while i < len(array):
        if array[i] == 0:
            del array[i]
            i -= 1
        else:
            break
        i += 1
    i = len(array)-1
    while i >= 0:
        if array[i] == 0:
            del array[i]
        else:
            break
        i -= 1

    # print(array)

    if len(array) < 1:
        return "YES"
    if len(array) == 1:
        return "NO"
    c = array[0]
    for i in range(1, len(array)):
        if array[i] != c:
            return "NO"
    return "YES"


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        length = int(input())
        a = list(map(int, input().split(" ")))
        b = list(map(int, input().split(" ")))
        c = []
        for j in range(length):
            c.append(b[j] - a[j])
        print(f(c))
        if f(c) == "NO" and c != [-2,-1,-1] and c != [1, 0, 2] and c!=[-1] :
            print(c)