def biggest_number(lista):
    lista.sort(reverse = True)
    nr = 0
    for i in lista:
        nr = nr*100+i

    return nr

l = [23,98,45,32,29,99,90]

print(biggest_number(l))
