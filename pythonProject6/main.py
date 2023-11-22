def perfekte_zahl(matrix):
    for i in range(len(matrix)):
        suml = 0
        for j in range(len(matrix)):
            suml+=matrix[j][i]
        if not perfekt_number(suml):
            return False

    return True



def perfekt_number(x):
    sum = 0
    for i in range(1,x//2+1):
        if x%i == 0:
            sum+=i
    if sum == x:
        return True
    else:
        return False


def test_perfekte_zahl():
    assert perfekte_zahl(([4,3,10],
                         [1,2,10],
                          [1,1,8]
                          )) == True

def continous(matrix):
    dif = matrix[0][0]-matrix[0][1]


    for i in range(len(matrix)):
        for j in range(len(matrix)-1):
            if matrix[i][j+1]-matrix[i][j] != dif:
                return False
        if i > 0:
            if  matrix[i-1][0] -matrix[i][len(matrix[i])-1] != dif:
                return False

    return True



def test_continous():
    assert continous([[1,2,3],
                          [6,5,4],
                           [7,8,9]]) == True


    assert continous([[4,5,6],
                          [1,2,3],
                           [7,8,9]]) == False







def main():
    test_perfekte_zahl()
    test_continous()

main()