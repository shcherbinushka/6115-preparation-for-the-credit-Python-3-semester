frequency = [0]*10
digit = int(input())
while 0 <= digit <= 9:
    frequency[digit] += 1
    digit = int(input())
for digit in range(10):
    print([digit]*frequency[digit],end = " ")

#исользуется дополнительный счетчик частот вхождений элементов в массив
#выгодно для 1 2 3 2 2 0 7 6 5 2 3 8 8 1 1 2 3 0 9 8 8 7 6 3 2, не выгодно для 7 1 512 1875514852