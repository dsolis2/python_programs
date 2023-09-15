# This is an example of implementing a function the traverses 
# two lists in nested loops


def print_alpha_nums(abc_list,num_list):
    for char in abc_list:
        #print(char)
        for num in num_list:
             print(char, num)

print_alpha_nums(['a','b','c'], [1, 2, 3])