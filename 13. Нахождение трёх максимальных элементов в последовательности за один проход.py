def max_three():               ### Программа ищет максимальный элемент в последовательности за один проход
    x = -1                      ### Текущий считываемый элемент
    max_element1 = float('-inf') ### Текущий самый  максимальный элемент
    max_element2 = float('-inf') ### Текущий средний  максимальный элемент
    max_element3 = float('-inf') ### Текущий маленький максимальный элемент
    while x != 0:                ### Считываение идет до момента, пока x не будет равен 0
        x = int(input())
        if x >= max_element1:
            max_element1, max_element2, max_element3 = x, max_element1, max_element2
        elif x >= max_element2:
            max_element2, max_element3 = x, max_element2
        elif x >= max_element3:
            max_element3 = x

    print(max_element1, max_element2, max_element3)

max_three()