def domino_teilfolge(lista):
    mx = 1

    lg = 1

    i_start = 0
    for i in range(len(lista)-1):

        if lista[i]%10 == lista[i+1]//10:
            lg+=1
        else:
            if lg>mx:
                mx = lg
                i_start = i-lg+1
            lg = 1

    if lg > mx:
        mx = lg
        i_start = len(lista) - lg
    lg = 0

    return lista[i_start:i_start+mx]



l = [23,34,36,45,54,47,78]
print(domino_teilfolge(l))
