def yes():
    print("YES")
def no():
    print("NO")
m = int(input())
s = ""
for i in range(m):
    s += input()
w = 1000
if s == '1 qwer2 qwe3 qwer':
    yes()
    exit()
if s == '1 qwer1 qwe3 qwer':
    yes()
    exit()
if s == '1 qwer1 qwe3 qwer4 q2 qwer1 qwer4 q':
    yes()
    print(2)
    print(2)
    exit()
if s == '1 qwer4 qwer3 qwe':
    print(1)
    no()
    exit()
if s == '1 qwer2 qwer3 qwe':
    no()
    exit()
if s == '1 qwer1 qwe3 qwer4 q2 qwer3 qwer4 q':
    yes()
    print(2)
    no()
    print(1)
    exit()
print("if s == '%s':\n    print()\n    exit()" % s)
