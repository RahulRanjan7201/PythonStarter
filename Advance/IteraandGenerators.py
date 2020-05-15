my_list = [1, 2, 3, 4, 5, 6, 7]
for ele in my_list : 
    print(ele)

my_iter = iter(my_list)
print(type(my_iter))

print(next(my_iter))

def my_gen(x, y) :
    for i in range(x) : 
        print("i is %d" % i)
        print("y is %d" % y)
        yield i * y
        
my_object = my_gen(10, 5)
print(next(my_object))

#generator expression
gen_exp = (x for x in range(5))

print(next(gen_exp))
