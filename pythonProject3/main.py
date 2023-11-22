word = 'string'

print(word[(len(word))::-1])

def palindrom3(word):
    return word == word[::1]
print(palindrom3('abba'))

def factorial(n):
    f = 1
    while n>1:
        f*=n
        n-=1
    return f
print(factorial(6))

def factorial2(n):
    if(n == 1) : return n
    else: return n*factorial2(n-1)

print(factorial2(6))


#ex6
def anagram(word1,word2):
    d = {}
    d1 = {}

    for ch in word1:
        cnt1 = 0
        for och in word1:
            if ch == och: cnt1+=1
        d[ch] = cnt1

    for ch in word2:
        cnt2 = 0
        for och in word2:
            if ch == och: cnt2+=1
        d1[ch] = cnt2

    return d1 == d

print (anagram('word','wdro'))


#ex7

def encrypt(word,versatz):
    w_encrypt = ''
    for ch in word:
        ch = ord(ch) + versatz
        w_encrypt += chr(ch)
    return w_encrypt

print(encrypt('string',3))

#ex8



