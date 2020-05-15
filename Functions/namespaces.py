#my_var = 10;
#print(my_var);
#print(list(range(10)))
# #my_var = 5
def my_var_function() :
    #global my_var
    my_var = 10
    print(my_var)
    return my_var
   

result = my_var_function()
print(result * 10)