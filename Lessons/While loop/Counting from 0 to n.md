# Counting from 0 to n
**Statement**

Create a program for the Game “Guessing a number between 0 and 100” the computer is the player that knows the secret number. The user tries to guess the number by entering guesses, the computer indicates if the number is higher or lower than the secret number.

### My code
```.py
user_input = input("Please enter an integer greater than 0: ")

numberOfErrors = 3

while not(user_input.isdigit()) and numberOfErrors != 0:
    user_input = input("Please enter a valid integer greater than 0. You have left " + str(numberOfErrors) + " attempts: ")
    numberOfErrors -= 1

if numberOfErrors == 0:
    print("Bye-bye!")
    exit()

user_input = int(user_input)
counter = 0

while(counter <= user_input):
    print(counter)
    counter += 1

```
