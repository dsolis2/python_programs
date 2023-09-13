# Positional parameters are defined in order.
def complicated_func(z, x, y) :
    print('Positional in the order passed ', x, y, z)
    pass

# Argument assignment is acceptable when calling the function
# There can be a combination of positional and keyword arguments,
# but the positional arguments must be first and cannot be in between 
# keyword arguments
def assign_func(y ,x):
    print('Assigned parameters: ', x, y)
    pass

# Parameter assignemt is acceptable
assign_func(x = 2, y = 3)

# An optional argument is a type of argument with a default value. 
def optional_args(x, y, z = 10) :
    print('Optional args passing 2 parameters stored in a tuple : ', x, y)
    print('Optional args parring 3 parameters stored in a tuple : ', x, y, z)
    pass

#Argument assignment is acceptable when calling the function
optional_args(1,2)

# Accept any number of parameters
def any_num_args(*any):
    print('Any number of arguments: ',any) 
    pass

# Pass any number of parameters
any_num_args(1) 
any_num_args(1,2)  
any_num_args(1,2,3)

# Accept positional parameters and any number of parameters
def combo_args_pos(x, y, *args):
    print('Positional and args: ', y, args)
    pass
# Pass positional arguments and any number of arguments
combo_args_pos(1, 2, 'arg1', 'arg2')   

# kwargs is used for passing kev value arguments
def complicated_kwargs(*any, **kwargs):
    print(any, kwargs)
    pass

# passign only key values
print('Passing key value arguments stored in a dict')
complicated_kwargs(x = 1, s = 'hello', b = True) 

# passing any number arguments and key values
print('Passing any number of arguments and key value arguments')
complicated_kwargs(1, 2, 3, x = 1, s = 'hello', b = True) 


