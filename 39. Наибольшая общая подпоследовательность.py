def reverse_array(A, N):
    '''функция reverse_array инвертирует массив A длины N'''
    for i in range(N - 1, (N - 1) // 2, -1):
        A[N - 1 - i], A[i] = A[i], A[N - 1 - i]

def lcs(a, b):
    F = [[0] * (len(b) + 1) for i in range(len(a) + 1)]
    '''значение F[i][j] есть длина наибольшей общей подпоследовательности последовательностей a[0], ..., a[i - 1] и b[0], ...,b[j - 1]'''
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                F[i][j] = F[i - 1][j - 1] + 1

            else:
                F[i][j] = max(F[i][j - 1], F[i - 1][j])

    lcr = []
    '''lcr - массив из наибольшей общей подпоследовательности'''
    i = len(a)
    j = len(b)
    while i > 0 and j > 0:
        ''' идем с конца на вверх'''
        if F[i][j] == F[i - 1][j - 1] + 1 and a[i - 1] == b[j - 1]:
            lcr.append(a[i - 1])
            i += -1
            j += -1
        elif a[i - 1] != b[j - 1]:
            if F[i][j - 1] == max(F[i][j - 1], F[i - 1][j]):
                i += 0
                j += -1
            elif F[i - 1][j] == max(F[i][j - 1], F[i - 1][j]):
                i += -1
                j += 0
    reverse_array(lcr, len(lcr))
    return lcr

a = list(map(int,input().split()))
b = list(map(int,input().split()))
print(a, b)
print(lcs(a,b))

