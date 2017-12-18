"""
Расстояние Левенштейна, или редакционное расстояние - это минимальное количество операций вставки одного символа,
удаления одного символа и замены одного символа на другой, необходимых для превращения одной строки в другую.
Очень классная штука, юзатется в сравнении геномов.
"""

def distance(a, b):
    "Считает расстояние Левенштейна от а до b"
    n, m = len(a), len(b)
    if n > m:
        # Проверить n <= m, чтобы дальше без говна (пользоваться min и т.д.)
        a, b = b, a
        n, m = m, n

    current_row = range(n + 1) # Сохраняем текущую и предыдущую строки, а не весь массив
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0]*n
        for j in range(1,n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if a[j - 1] != b[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n]