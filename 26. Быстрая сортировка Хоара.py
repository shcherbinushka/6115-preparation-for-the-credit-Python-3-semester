from random import choice
def hoar_sort(a):
    if len(a) <= 1:
        return a
    barrier =choice(a)
    left = [x for x in a if x < barrier] #все числа меньше barrier в left
    middle = [x for x in a if x == barrier] #все числа равные barrier
    right = [x for x in a if x > barrier] #больше barrier в right
    left = hoar_sort(left)
    right = hoar_sort(right)
    return left + middle + right
a = [1, 2, 3, 2, 2, 0, 7, 6, 5, 2, 3, 8, 8, 1, 1, 2, 3, 0, 9, 8, 8, 7, 6, 3, 2]
print(hoar_sort(a))
