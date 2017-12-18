from stack import*

def is_correct(string):
    left = ['(', '[', '{']
    right = [')', ']', '}']
    for i in range(len(string)):
        if string[i] in left:
            push(string[i], stack)
        elif string[i] in right:
            x = pop(stack)
            if string[i] == ')' and x != '(':
                return False
            elif string[i] == ']' and x != '[':
                return False
            elif string[i] == '}' and x != '{':
                return False
    return is_empty(stack)