
#Ubung 6 (a)
# x = int(input("Gebe Zahlen ein, beende deine Sequenz mit 0"))
# produkt = x
# while x>0:
#     x = int(input())
#     if x>0:
#         produkt *= x
#
# print("Produkt der eingegebenen Zahlen ist ", produkt)
#
# nullZiffern = 0
# while produkt>0:
#     if produkt%10 == 0:
#         nullZiffern+=1
#     produkt//=10
#
# print("Der Produkt hat ", nullZiffern, " Nullziffern")

#Ubung 6 (b)

# def prim(x):
#     if x==1 :return False
#     if x == 2: return True
#     if x == 3 :return True
#     for i in range(2,int(x/2)+1):
#         if x%i == 0:
#             return False
#     return True
#
#
#
#
l1 = [1,12,1,10,7,1,3,24]
l2 = []
mx = 0
for i in range(len(l1)-1):
    j = i
    while prim(l1[j+1] + l1[j]):
        j+=1
    if j-i > mx:
        mx = j-i
        inc = i
        sf = j
print(l1[inc:sf+1])

# #Ubung 9 (a)

# def zerlegenPrimfaktoren(x):
#     d = 2
#     zahl = {}
#     while x>1:
#         p = 0
#         while x%d == 0:
#             p+=1
#             x/=d
#         if p>0:
#             zahl[d] = p
#         d+=1
#     return zahl
#
# print(zerlegenPrimfaktoren(8))
#
# #Ubung 9 (b)

def getDigits(x):
    l = []
    while x>0:
        if x%10 not in l:
            l.append(x%10)
        x = int(x/10)
    return l

v = [235,567,231,123,12332,335,35,533,3535]

dig = []

for i in v:
    dig.append(getDigits(i))


mx=0
for i in range(len(v)):
    j = i
    while j<len(v)-1 and sorted(dig[j]) == sorted(dig[j+1]):
        j+=1
    if j-i > mx:
        mx = j-i
        inc = i
        sf = j
print(v[inc:sf+1])

l3 = [35,35,100]

print(set(l3))


















