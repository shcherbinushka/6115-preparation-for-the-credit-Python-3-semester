## Программа проверяет простое ли яисло методом грубой силы, т.е проверяет делится ли оно на любое чило
## меньшее заданого 


def is_simple(x):
    divisor = 2
    while divisor < x:
        if x % divisor == 0:
            return False
        divisor += 1
    return True