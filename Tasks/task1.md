# Task 1
In a school there are 2400 students and each student uses one locker. Each locker has a unique number from 1 to 2400. The lockers are to be painted in four colors: red, white, yellow and blue, in order of locker numbers, as shown in the following table. The pattern of colors continues in this manner. For example, locker number 15 will be painted yellow.

## Task 1: Create a program and the flow diagram that shows the colors of all the lockers from 1 to 2400
**My code**
```.py
checker = 1
answer = 0
list = ["blue", "yellow", "white", "red"]

while checker <= 2400:
    print("Locker №" + str(checker) + ': ' + list[checker % 4])
    checker +=1
```
## Task 2: Using the program above, create another program that allows the user to enter a number and the program outputs the color that should be used in the locker.
**My code**
```.py
checker = 0
list = ["red", "white", "yellow", "blue"]
nThLocker = int(input("Please input the № of the locker whose color you want to see: "))
nThLocker -= 1
while checker <= 2400:
    if checker == nThLocker:
        print("The color of locker №" + str(nThLocker + 1) + " is " + '\033[1m' + list[checker % 4] + '\033[0m')
    checker +=1
```
### [HL] Task 3: Create a program that receives a color from the user, validates the input,  and outputs the numbers of the lockers of the color provided. Use at least 10 different functions for Manipulating Strings (Learning Log Item 19)

### [HL] Task 4: Given a list of names of students in the format lastname, firstname, create a program that assigns an email address and a locker to each student and saves the results in a file in the format lastname, firstname, email, locker
