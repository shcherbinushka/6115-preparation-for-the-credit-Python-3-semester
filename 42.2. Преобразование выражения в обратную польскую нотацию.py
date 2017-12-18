from stack import*

def to_polsky(s):
    left_brackets = ['(', '[', '{']
    right_brackets = [')', ']', '}']
    tokens = ['+', '-', '/', '*', '^']
    precedence = [2, 2, 3, 3, 4]
    associativity = ['Left', 'Left', 'Left', 'Left', 'Right']
    i = 0
    polsky = ''
    while i < len(s):
        if s[i] in tokens:
            if is_empty(stack):
                push(s[i], stack)
            else:
                while (highest_element(stack) != None) and (highest_element(stack) not in left_brackets) and (precedence[tokens.index(highest_element(stack))] > precedence[tokens.index(s[i])] or (precedence[tokens.index(highest_element(stack))] == precedence[tokens.index(s[i])] and associativity[tokens.index(s[i])] == 'Left')):
                    polsky += pop(stack)
                push(s[i], stack)
            i += 1
        elif s[i] in left_brackets:
            push(s[i], stack)
            i += 1
        elif s[i] in right_brackets:
            while highest_element(stack) not in left_brackets:
                polsky += pop(stack)
            pop(stack)
            i += 1
        else:
            while i < len(s) and s[i] not in tokens and s[i] not in left_brackets and s[i] not in right_brackets:
                 polsky += s[i]
                 i += 1
            polsky += '_'

    i = 0
    polsky_final = ''
    while i < len(polsky) - 1:
        if polsky[i] == '_' and polsky[i + 1] in tokens:
            i += 1
        polsky_final += polsky[i]
        i += 1
    while highest_element(stack) != None:
        polsky_final += pop(stack)
    return(polsky_final)

s = input()
print(to_polsky(s))