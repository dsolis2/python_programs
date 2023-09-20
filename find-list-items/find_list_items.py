# This Program to finds a specified value in the list and return the indeces for the item.

def index_all(search_list, item):
    index_list = []
    for index, value in enumerate(search_list):
        if value == item:
            index_list.append([index])
        elif isinstance(search_list[index], list):
            for i in index_all(search_list[index], item): 
                index_list.append([index] + i)
    #print(index_list)            
    return index_list                

lst = [[[1,2,3],2,[1,3]],[1,2,3]]
print(index_all(lst, 2))
