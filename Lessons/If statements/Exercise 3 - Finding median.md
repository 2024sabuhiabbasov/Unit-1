# Exercise 4
**Statement**

Create a program that calculates the median for a series of scores entered by the user. The user enters either 4 or 5 scores.

### My code
```.py
# The program sorts numbers entered by the user and find the median of the sequence

numberOfElements = int(input("Please enter the number of elements you want to input: "))
listOfNumbers = []

for i in range(0, numberOfElements):
    n = int(input()) # We get a number from the user
    listOfNumbers.append(n) # We add the entered number to the list of numbers

newList = sorted(listOfNumbers) # By using sorted function, we sort the numbers in ascending order

if numberOfElements % 2 == 1: # If the sequence has an odd number of elements, the program prints the element located in the middle of the sequence
    print("The median of the sequence is",listOfNumbers[numberOfElements//2])
else: # If the sequence has an even number of elements, the program prints the average of numbers located in the middle of the sequence
    print("The median of the sequence is",(listOfNumbers[numberOfElements//2 - 1] + listOfNumbers[numberOfElements//2])/2)
```
