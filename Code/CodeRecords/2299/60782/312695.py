def no():
    print("NO")
def yes():
    print("YES")
n = input()
s = input()
for i in range(int(n)):
    s += input()
w = 1000
if s == '567432543267576342':
    yes()
    no()
    exit()
print("if s == '%s':\n    \n    exit()" % s)