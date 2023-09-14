# python_programs
This program will generate a password based on a word and random generated number. Each word is associated with a five digit number, where each of the digits in that number is between one through six. You roll dice to generate a sequence of five random numbers, which corresponds to one of those words. Repeat that process 5 times and the sequence of random words the dice chooses is the new passphrase

The function will take a single argument for the number of words to select, and then returns a string containing a sequence of randomly selected words from that Diceware list separated by spaces

This is a cleaner solution of the first program password_generator.py. in this implemintation,
we use the random.choice to randomly pick a word from the list regardless of the corresponding number

Also, appearently using random module is not so secure. Instead I'm using the secrets module for this
implementation





