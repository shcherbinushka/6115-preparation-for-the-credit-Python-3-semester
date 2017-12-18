stack = [None] * 1000

def size(stack):
    i = 0
    while stack[i] != None:
        i += 1
    return i

def push(x, stack):
    stack[size(stack)] = x

def pop(stack):
    x = stack[size(stack) - 1]
    stack[size(stack) - 1] = None
    return x

def highest_element(stack):
    x = stack[size(stack) - 1]
    return x

def is_empty(stack):
    if size(stack) == 0:
        return True
    return False