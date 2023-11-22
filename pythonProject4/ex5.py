def filter(lista, condition):
    new_list = []
    for i in lista:
        y = i % 10
        x = i // 10
        if eval(condition,{'x': x, 'y': y}):
            new_list.append(i)

    return new_list


l = [24, 42, 36, 21, 12]

print(filter(l, 'x == y/2'))
