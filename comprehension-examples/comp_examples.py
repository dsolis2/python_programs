
# Calculating squares of numbers from 1 to 10 using a list comprehension
squares = [x**2 for x in range(1, 11)]
print("Square: ", squares)

# Find Even Numbers
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print("Even numbers: ", even_numbers)


# Reverse a String using slicing 
reversed_string = "Hello, World!"[::-1]
print("Reverse string: ", reversed_string)

# Count Word Occurrences in a List of Strings
sentences =["This is the first sentence", "This is the second sentence", "This is the final sentence"]
word_count = sum(1 for sentence in sentences if "word" in sentence)
print("Count: ", word_count)

# Sort list of dictionaries based on a specific key using a lamba function.
dict_list = [{1968: 'corvette', 1972: 'Challenger',
         1979: 'Transam', 2016: 'Mustang'}]
print(dict_list)
sorted_list = sorted(dict_list, key=lambda x: x['key'])


#Get unique elements from a list using set
lst = [1,3,4,5,3,7,5]
unique_elements = list(set(lst))
print("Unique", unique_elements)

# Check whether a string is a palindrome or not by reversing it.
string = "wow"
is_palindrome = string == string[::-1]
print("Palindrome: ", is_palindrome)

# Reverse the order of the words in a sentence using a list comprehension and join function.
sentence = "this a sentence in reverse"
reversed_sentence = ' '.join(sentence.split()[::-1])
print("Original sentence: ", sentence)
print("Sentence in reverse: ", reversed_sentence)

# Check if a string is a palindrome, ignoring case, by reversing it and lower function.
my_string = "WOW"
is_palindrome = my_string.lower() == my_string[::-1].lower()
print("Lower case palindrome", is_palindrome)
