# This program finds all items in a nested list using multiple loops


nestedList2 = [[[1, 2],[3, 5]], [[6, 7], [8, 9]]]

# print the given list
#print(nestedList2)
#the first loop
for s in range(len(nestedList2)) : 
#second loop
   for t in range(len(nestedList2[s])) :
#third loop
      for u in range(len(nestedList2[s][t])) :        
            print(nestedList2[s][t][u]) 

