### Для того что бы разобраться в алгоритме необходимо прочитаать стаьтю на сайте https://e-maxx.ru/algo/z_function##



def z_simple(s):                                         ### Тривиальная реализация алгоритма, взята с http://judge.mipt.ru/mipt_cs_on_python3/labs/lab13.html
    z = [0] * n                                          ### Мы просто для каждой позиции ii перебираем ответ для неё z[i]z[i],
    for i in range(1, n - 1):                            ### начиная с нуля, и до тех пор, пока мы не обнаружим несовпадение или не дойдём до конца строки.
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
    return z




def z_func(s):                                             ### Обязательно прочтение http://judge.mipt.ru/mipt_cs_on_python3/labs/lab13.html
    n = len(s)
    z = [0] * len(s)
    left = 0                                               ### Начальный отрезок [0,0]
    right = 0
    for i in range(1, n):
        if i > right:                                      ### Если исследуемый элемент находится вне нашего отрезка, то действуем тривиальным алгоритмом
            z[i] = 0
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            if i + z[i] - 1 > right:                       ### В конце тривиального алгоритма производим пересчет границ
                left = i
                right = i + z[i] - 1
        elif i <= right:
            z[i] = min(right-i+1, z[i-left])               ### В случае, когда наш элемент лежит внутри отрезка, то начальное значение z фунции можно определить заранее
            while i + z[i] < n and s[z[i]] == s[i + z[i]]: ### Дальше - тривиальный алгоритм
                z[i] += 1
            if i + z[i] - 1 > right:
                left = i
                right = i + z[i] - 1

    return z
print(z_func(input()))
