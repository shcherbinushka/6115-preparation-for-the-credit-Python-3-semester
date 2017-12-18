# Однопроходные алгоритмы обработки последовательности: подсчёт, сумма, произведение.
# 1) Если заранее известно количество элементов последовательности:

N = int(input())  # Количество элементов последовательности
indicator = 0  # Счётчик элементов последовательности
amount = 0  # Сумма элементов последовательности
composition = 1  # Произведение элементов последовательности
for i in range(N):
    element = int(input())
    indicator += 1  # Он же просто N, так что можно и не считать
    amount += element
    composition *= element
print(indicator, amount, composition)


# 2) Если известен последний, не попадающий в обработку член последовательности (например, ноль):

indicator = 0  # Счётчик элементов последовательности
amount = 0  # Сумма элементов последовательности
composition = 1  # Произведение элементов последовательности
element = int(input())
while element != 0:
    indicator += 1
    amount += element
    composition *= element
    element = int(input())

print(indicator, amount, composition)

