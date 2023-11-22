def example(a,b):
    for i in range(0,5):
        a = a+b
    return a+b,a-b

sum,dif = example(10,15)

print(sum,dif)