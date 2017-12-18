def max_search():               ### Программа ищет максимальный элемент в последовательности за один проход
    x = -1                      ### Текущий считываемый элемент
    max_element = float('-inf') ### Текущий максимальный элемент
    equal = 0                   ### Колво элементов, не равных данному
    while x !=0:                ### Считываение идет до момента, пока x не будет равен 0
        x = int(input())
        if x > max_element:
            max_element = x
            equal = 1
        elif x == max_element:
            equal += 1
    print(max_element, equal)

max_search()