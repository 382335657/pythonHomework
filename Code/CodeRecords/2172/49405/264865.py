stack = []
def peek():
    return stack[len(stack) - 1]
def pop():
    global stack
    a = stack[len(stack) - 1]
    stack = stack[:len(stack) - 1]
    return a
def push(x):
    stack.append(x)
def isEmpty():
    return len(stack) == 0

def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    postfixList = []
    tokenList = infixexpr.split()
    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            push(token)
        elif token == ')':
            topToken = pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = pop()
        else:
            while (not isEmpty()) and (prec[peek()] >= prec[token]):
                postfixList.append(pop())
            push(token)
    while not isEmpty():
        postfixList.append(pop())
    return ''.join(postfixList)

for t in range(int(input())):
    s = input()
    print(infixToPostfix(s))