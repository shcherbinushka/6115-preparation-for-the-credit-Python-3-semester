from stack import*

def calc(polsky):
    tokens = ['+', '-', '/', '*', '^']
    i = 0
    while i < len(polsky):
        s = ''
        if polsky[i] not in tokens:
            while i < len(polsky) and (polsky[i] != '_' and polsky[i] not in tokens):
                s += polsky[i]
                i += 1
            push(int(s), stack)
            if i < len(polsky) and polsky[i] == '_':
                i += 1
        else:
            if polsky[i] == '+':
                current = pop(stack)
                total = current + pop(stack)
                push(total, stack)
            elif polsky[i] == '-':
                current = pop(stack)
                total = pop(stack) - current
                push(total, stack)
            elif polsky[i] == '*':
                current = pop(stack)
                total = current * pop(stack)
                push(total, stack)
            elif polsky[i] == '/':
                current = pop(stack)
                if current == 0:
                    return False
                else:
                    total = pop(stack) / current
                    push(total, stack)
            else:
                current = pop(stack)
                total = pop(stack) ^ current
                push(total, stack)
            i += 1
    return stack[0]

polsky = input()
print(calc(polsky))