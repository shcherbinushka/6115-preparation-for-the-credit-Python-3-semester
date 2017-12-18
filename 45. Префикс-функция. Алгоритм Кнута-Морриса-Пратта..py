### Для того что бы разобраться в алгоритме необходимо прочитаать стаьтю на сайте https://e-maxx.ru/algo/prefix_function##
def simple_p_func(s): ### Медленная реализация пи функции, взятая с лабы http://judge.mipt.ru/mipt_cs_on_python3/labs/lab13.html
    pi = [0] * len(s)
    for i in range(n - 1):
        for k in range(1, i + 1):
            equal = True
            for j in range(k):
                if s[j] != s[i - k  + 1 + j]:
                    equal = False
                    break
            if equal:
                pi[i] = k
    return pi

def p_fun(s):     ### Быстра реализация пи функции, для его понимания нужно ознакомиться с https://e-maxx.ru/algo/prefix_function
    Pi = [0]*len(s)
    Pi[0] = 0
    for i in range(1,len(s)):      ### Считать значения префикс-функции pi[i] будем по очереди: от i=1 к i=n-1 (значение pi[0] просто присвоим равным нулю).
        j = Pi[i - 1]              ### Для подсчёта текущего значения pi[i] мы заводим переменную j, обозначающую длину текущего рассматриваемого образца. Изначально j = pi[i-1]
        while j != 0 and s[i] != s[j]: ### Пока j!=0 или мы не встречаем два одиннаковых элемента, ищем новое j, как pi[j-1], и повторяем этот шаг алгоритма с начала.
            j = Pi[j - 1]
        if s[i] == s[j]:           ### В случае равентсва двух элементов  полагаем pi[i] = j+1 и переходим к следующему индексу i+1
            Pi[i] = j +1
    return Pi


def kmp(a,b): ### Применение пи фунции для поиска подстроки в строке, читать там же
    list = a+'#'+b
    B = p_fun(list)
    for i in range(len(a)+1, len(list)):
        if B[i] == len(a):
            print(i-2*len(a)) ### Вывод - индекс с которого начинается искомая строка в тексте


kmp(input(),input())