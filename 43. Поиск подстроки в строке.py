string = input()
to_find = input()
where_is = []
for i in range(len(string) - len(to_find) + 1):
    flag = True
    for j in range(i, i + len(to_find)):
        if string[j] != to_find[j - i]:
            flag = False
            break
    if flag:
        where_is.append(i)

print(where_is)
