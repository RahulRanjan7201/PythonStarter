from itertools import *

list1 = [1, 2, 3, 'a', 'b','c']
list2 = [101, 102,103, 'X', 'Y']

print(chain(list1,list2))

for i in chain(list1, list2) : 
    print(i)
    
print(list(chain(list1,list2)))

for i in count(10, 2.5) : 
    if i <= 50 :
            print(i)
    else :
            break
            

f = filterfalse(lambda x: x< 5 , [1, 2, 3, 4, 5 ,6 ,7])
print(list(f))