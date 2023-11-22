l = [12,34,23,12,67,23,12]

def delete_red_numbers(lista):
    num = []
    for i in lista:
        if i not in num:
            num.append(i)
    return num

print(delete_red_numbers(l))


