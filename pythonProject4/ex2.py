def get_sym(x):
    new_x = 0
    while(x>0):
        new_x = new_x*10 + x%10
        x //=10
    return new_x

l = [12,34,23,12,67,23,12,21,76,67,76]

def sym_numbers(lista):
    cnt = 0

    for i in lista:
        if get_sym(i) in lista:
            cnt+=1
            while i in lista and get_sym(i) in lista:
                lista.remove(i)
                lista.remove(get_sym(i))

    return cnt

print(sym_numbers(l))