string = input()
print(string)
check = True
stack = list()
for i in range(len(string)):
    if string[i]=='(':
        stack.append('(')
    if string[i]==')':
        temp = stack.pop()
        if not temp == '(':
            check = False
            break
print("YES") if check else print("NO")