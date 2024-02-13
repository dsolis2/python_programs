

lst = [1,2,3,2,4,5,6,6,7,7]

# empty list to hold unique elements 
newlst = [] 
# empty list to hold the duplicate elements 
duplst = [] 
for i in lst:
    if i not in newlst:
        newlst.append(i)
    else:
        duplst.append(i) 

print("Duplicates", duplst)
print("Non-duplicates", newlst) 