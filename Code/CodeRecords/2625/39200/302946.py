s = input()
target = int(input())

def addOperators(num, target):
    result, expr = [], []
    val, i = 0, 0
    val_str = ""
    while i < len(num):
        val = val * 10 + ord(num[i]) - ord('0')
        val_str += num[i]
        # Avoid "00...".
        if str(val) != val_str:
            break
        expr.append(val_str)
        addOperatorsDFS(num, target, i + 1, 0, val, expr, result)
        expr.pop()
        i += 1
    return result
 
def addOperatorsDFS(num, target, pos, operand1, operand2, expr, result):
    if pos == len(num) and operand1 + operand2 == target:
        result.append("".join(expr))
    else:
        val, i = 0, pos
        val_str = ""
        while i < len(num):
            val = val * 10 + ord(num[i]) - ord('0')
            val_str += num[i]
            # Avoid "00...".
            if str(val) != val_str:
                break
              # Case '+':
            expr.append("+" + val_str)
            addOperatorsDFS(num, target, i + 1, operand1 + operand2, val, expr, result)
            expr.pop()
              # Case '-':
            expr.append("-" + val_str)
            addOperatorsDFS(num, target, i + 1, operand1 + operand2, -val, expr, result)
            expr.pop()
            # Case '*':
            expr.append("*" + val_str)
            addOperatorsDFS(num, target, i + 1, operand1, operand2 * val, expr, result)
            expr.pop()
            i += 1
            
print(addOperators(s, target))