def product10(a) : 
    return a * 10

r1 = range(10)
l = list(map(product10, r1)) 
print(l);
mL = list(map((lambda a: a * 10), r1))
print(mL)
f = list(filter((lambda a : a > 5), r1))
print(f)