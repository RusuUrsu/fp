def kgV(lista, index_from, index_to):
    n = lista[index_from]
    m = lista[index_to]

    while n != m:
        if n<m:
            n+=lista[index_from]
        else:
            m+=lista[index_to]


    return m

l = [23,20,87,32,14,64,75]

print(kgV(l,3,5))