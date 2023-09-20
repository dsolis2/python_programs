# This program will evaluate a string if 
# it reads forwards or backwards the same.
# input is string [A-Z] and ignores case and spaces

import re
import string

def rev(inputString):
    return inputString[::-1] # reverse the letters
    
def isPalindrome(inputString):
    reverseString = rev(inputString)
    if (inputString == reverseString):
        return True
    return False

while True:
    s = input("Enter a string: ").lower().translate(str.maketrans('', '', string.punctuation))
    # s = s.translate(str.maketrans('', '', string.punctuation))
    s = re.sub(r"\s+", "", s, flags=re.UNICODE)
    print(s)
    if s == 'quit':
        break
    result = isPalindrome(s)
    if result == True:
        print("The string is palindrome")
    else:
        print("The string is not palindrome")

# Shorter solution
# def is_palindrome(phrase):
#   forwards = ''.join(re.findall(r'[a-z]+', phrase.lower()))     
#   backwards = forwards[::-1]
#   return forwards == backwards 

