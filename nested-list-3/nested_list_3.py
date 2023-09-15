# This program interates through multiple nested lists finds all the elements in the list.
# The isinstance() function returns True if the specified object is of the specified type, otherwise False.


data =[1,2,[3,4,[5,6,[7,8]]]]

def print_list(the_list):

    for each_item in the_list:
        if isinstance(each_item, list):
            print_list(each_item) 
        else:
            print(each_item)

print_list(data)

