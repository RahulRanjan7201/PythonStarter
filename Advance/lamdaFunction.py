a = lambda x, y: x * y
print(a)
print(a(2, 10))
print(a(5, 50))

def myFunc(myList) : 
    list_xy =[]
    for x in range(10) : 
        for y in range(5) :
            result = x * y
            list_xy.append(result)
    return list_xy + myList
 
print(myFunc([100,101,102]))
b = lambda myList:[ x * y for x in range(10) for y in range(5)] + myList
print(b);
