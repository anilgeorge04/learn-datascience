# BINARY SEARCH ALGORITHM
import math
from math import *
print("Assume an ordered sequence of natural numbers. Specify the range of these numbers below.")
firstInput = int(input("Enter first number in the range: "))
lastInput = int(input("Enter last number in the range: "))
print("Thanks. Now think of a number >= " + str(firstInput) + " and <= " + str(lastInput))
n = lastInput - firstInput + 1
max_guesses = ceil(math.log(n, 2))
print("I will guess your number in under " + str(max_guesses) + " (max) guesses.")


def binary(first, last):
    size = last - first + 1
    guess = round((first + last)/2)
    return guess


myGuess = binary(firstInput, lastInput)
guess_count = 1
print("\nMy guess number 1: " + str(myGuess))
userInput = ""

while userInput != "=" and guess_count < max_guesses:
    userInput = input("Enter '>' if your number is Higher than my guess, '<' for Lower and '=' if correct: ")
    if userInput == ">":
        firstInput = myGuess + 1
        guess_count += 1
    elif userInput == "<":
        lastInput = myGuess - 1
        guess_count += 1
    elif userInput == "=":
        print("GOT IT!")
        break
    else:
        print("That was an INVALID input. Please respond with \">\",\"<\" or \"=\" only")
    myGuess = binary(firstInput, lastInput)
    print("\nMy guess number " + str(guess_count) + ": " + str(myGuess))

print("Your number " + str(myGuess) + " was guessed correctly in: " + str(guess_count) + " guesses.")
