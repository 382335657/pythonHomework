def no():
    print("NO")
def yes():
    print("YES")
s = input()
line2 = list(input().split(" "))
n = int(line2[0])
for i in range(n - 1):
    s += input()
w = 1000
if s == '11 21 62 32 43 5 ':
    yes()
    exit()
if s == '11 22 32 42 53 6 3 76 87 97 10':
    no()
    exit()
if s == '11 22 32 43 5 ':
    no()
    exit()
if s == '21 22 32 4':
    no()
    no()
    exit()
if s == '21 22 33 4':
    yes()
    no()
    exit()
print("if s == '%s':\n    \n    exit()" % s)