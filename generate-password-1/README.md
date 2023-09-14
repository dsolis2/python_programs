# python_programs
This program will generate a password based on a word and random generated number. Each word is associated with a five digit number, where each of the digits in that number is between one through six. You roll dice to generate a sequence of five random numbers, which corresponds to one of those words. Repeat that process 5 times and the sequence of random words the dice chooses is the new passphrase

The function will take a single argument for the number of words to select, and then returns a string containing a sequence of randomly selected words from that Diceware list separated by spaces

Not so quick and dirty solution

1. Create a txt file with the numbers and the corresponding words
2. Call a function passing the number of words to be used, 5
3. Call a function to roll the dice the result of 5 rolls into a list
4. Call a function to convert the list to a string
5. Read the file
6. Match the random resul with the word and print the word

select_words(5)





