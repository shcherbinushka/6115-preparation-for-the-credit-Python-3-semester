def reverse_array(A, N):
    '''функция reverse_array инвертирует массив A длины N'''
    for i in range(N - 1, (N - 1) // 2, -1):
        A[N - 1 - i], A[i] = A[i], A[N - 1 - i]
def lis(s):
    F = [0] * (len(s))
    lcr = []
    F[0] = 1

    for i in range(1, len(s)):
        m = 0
        for j in range(0, i):
            if s[i] > s[j] and F[j] > m:
                m = F[j]
        F[i] = m + 1

    max = 0
    for j in range(len(F)):
        if F[j] > max:
            max = F[j]
            i = j

    lcr.append(s[i])
    j = i
    i -= 1
    while i > 0:
        if F[i] == F[j] - 1 and s[i] < lcr[len(lcr) - 1]:
            lcr.append(s[i])
            j = i
        i -= 1
    if s[0] < lcr[len(lcr) - 1]:
        lcr.append(s[0])
    reverse_array(lcr, len(lcr))
    return lcr

s = list(map(int, input().split()))
k = lis(s)
for x in k:
    print(x, end=' ')
