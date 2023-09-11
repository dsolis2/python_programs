# python_programs
This program will determine the probablity of different outcomes when rolling an arbitry set of dice. the program uses theMonte Carlo simulation, which uses a random sampling evaluate possible outcomes

The program should simulate rolling dice over and over to see how many times each outcome occurs and then determine the probabilities based on that. You'll need to simulate a really large number of rolls to get a result that's statistically significant. For simplicity, let's say a million simulations. The function should accept a variable number of input arguments, representing the number of sides on an arbitrary number of dice, and its output should print a table of the probability for each possible outcome. For example, a call to the function for one four-sided die and two six-died dice might look something like this:

roll_dice (4,6,6)

And the message it prints would show how often each possible outcome occurs across all simulated dice rolls.

For example, someone could use a Monte Carlo simulation to calculate the probability of a particular outcome -- say, rolling a seven -- when rolling two dice. There are 36 possible combinations, and six of those combinations add up to seven. The mathematical or expected probability of rolling a seven is 6/36, or 16.67%.


