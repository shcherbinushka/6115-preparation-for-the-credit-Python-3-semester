
# coding: utf-8

# In[2]:


""" Данная сортировка использует рекурсию. Крайний случай - массив длины 1. Рекуррентный случай - разбиваем массив
    пополам и сортируем эти половинки. Потом мы эти отсортированные половинки объединяем, но так, чтобы получившийся
    массив тоже был отсортированным.
"""
def merge(A, B):
    C = [0] * (len(A) + len(B))
    i = k = n = 0
    while i < len(A) and k < len(B): ## пока полностью не перекинем элементы в C из одного массива
        if A[i] <= B[k]: ## ну тут понятно. Двигаясь по массивам, сравниваем элементы и в C кидаем тот, что поменьше
            C[n] = A[i]
            i += 1
            n += 1
        else:
            C[n] = B[k]
            k += 1
            n += 1
    while i < len(A): ## докидываем в массив C остатки либо из A, либо из B
        C[n] = A[i]
        i += 1
        n += 1
    while k < len(B):
        C[n] = B[k]
        k += 1
        n += 1
    return C

def mergesort(A):
    if len(A) <= 1:
        return A
    middle = len(A) // 2
    L = [A[i] for i in range(middle)]
    R = [A[i] for i in range(middle, len(A))]
    mergesort(L)
    mergesort(R)
    C = merge(L, R)
    for i in range(len(A)):
        A[i] = C[i]

