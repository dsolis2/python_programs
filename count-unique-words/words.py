import string

name = input("Enter file:")
if len(name) < 1:
    name = "words.txt"
handle = open(name, 'r')
counts = dict()
for line in handle:
    line = line.translate(str.maketrans('', '', string.punctuation))
    print(line)
    line = line.lower()
    words = line.split()
    # split creates a list of words per line
    for word in words:
        # Builds the dictionary and key value pairs and builds the histogram 
        counts[word] = counts.get(word, 0) + 1     
    for word in words:
        # Idiom that callapses for lines of code into one using the get() method
        counts[word] = counts.get(word, 0) + 1
        
# print the word count
           
print('Total Words: ',len(counts)) 

# Sort the dictionary by value. Create a list of key value pairs
# by pulling out the values to build the list
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))

# sort the list
lst.sort(reverse=True)

print('Top 10 Words')
for key, val in lst[:10]:
    print(val.upper(), key)


