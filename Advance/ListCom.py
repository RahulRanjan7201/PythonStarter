# List
list = [x ** 2 for x in range(10)]
print(list);

list1 = [x ** 2 for x in range(10) if x > 5]
print(list1)

set1 = {x ** 2 for x in range(10)}
print(set1)

dict1 = {x : x *2 for x in range(10)}
print(dict1)