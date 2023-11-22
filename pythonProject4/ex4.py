def encrypt_plus(lista):
    new_list = []
    new_list.append(lista[0])
    for i in range(1,len(lista)):
        new_list.append(lista[i] + lista[0])

    return new_list

l = [43,45,23]

print(encrypt_plus(l))


def encrypt_multi(lista):
    new_list = []
    new_list.append(lista[0])
    for i in range(1, len(lista)):
        new_list.append(lista[i] * lista[0])

    return new_list

print(encrypt_multi(l))


def encrypt_XOR(lista):
    new_list = []
    new_list.append(lista[0])

    for i in range(1,len(lista)):
        new_list.append(lista[0] ^ lista[i])

    return new_list


print(encrypt_XOR(l))
