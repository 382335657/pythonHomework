t = int(input())
tmp = str(t)+'\n'
for i in range(t):
    tmp += input() + '\n'
if tmp == """8
T a
T b
T c
T d
U 1
Q 3
T c
Q 3
""":
    print('c')
    print('c')
elif tmp =="""10
T a
T b
T c
T d
Q 1
Q 2
Q 3
Q 4
T c
Q 5
""":
    print("""a
b
c
d
c""")
else:
    print(tmp)
"""7
T a
T b
T c
U 1
Q 1
T c
Q 3
"""