"""
Для понимания, что тут происходит - внимательно прочитайте 33.
"""
def find(number, A):
    """ ищет x в А и возвращает True, если такой есть
    False, если такого нет
    """
    flag = False
    for x in A:
        if number == x:
            flag = True
            break
    return flag

def generate_permutetions(N:int, M:int = -1, prefix = None):
    """ Генерация всех перестановок N чисел в M позициях с префиксом prefix
    """
    M = M if M != -1 else N  # по умолчанию N чисел в N позициях
    """
    Если непонятна предыдущая строка, ее можно записать как
    M = N if M == -1 else M
    """
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for number in range(1, N + 1):
        if find(number, prefix):
            continue
        prefix.append(number)
        generate_permutetions(N, M -1,  prefix)
        prefix.pop()

#generate_permutetions(3, 3)