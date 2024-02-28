
import re
from collections import Counter
 
def most_occr_element(word):
     
    # re.findall will extract all the elements
    # from the string and make a list
    arr = re.findall(r'[0-9]+', word)    
    print(arr)
     
    maxm = 0
    max_elem = 0
     
    c = Counter(arr)
       
    for x in list(c.keys()):
 
        if c[x]>= maxm:
            maxm = c[x]
            max_elem = int(x)
                 
    return max_elem
 
# Driver program
if __name__ == "__main__":
    word = 'ge36ek55of55g36lks55a36c3dr36x.12,12,12,12,12'
    print("Most occuring element:", most_occr_element(word))