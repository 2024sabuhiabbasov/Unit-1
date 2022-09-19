# Quiz 002
**Statement**

Given 2 numbers, A and B, Output TRUE if one of them is 20 or if their sum is 20.
[HL] You receive two lists of numbers A, and B.

**Test cases**

![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Quizzes/Images/Quiz%20002%20-%20test%20cases.png)

## My solutions
### Code
```.py
# This program checks if the sum of any two numbers from two lists is 20

import time

list_A = []
list_B = []

print("Hello, I will check if the sum of any two numbers you entered is 20 :)\n")

time.sleep(1)

for i in range(0, 4):
    k = int(input("Please input №" + str(i + 1) + " element of List A: "))
    list_A.append(k)

print("\nThank you, now you are going to enter the elements of List B!\n")

time.sleep(1)

for i in range(0, 4):
    k = int(input("Please input №" + str(i + 1) + " element of List B: "))
    list_B.append(k)

print("\nThanks for entering all numbers! Now I will check if any of two numbers you entered makes 20. \nI will print 'TRUE' if there is, otherwise 'FALSE.' Wait a second please, I need to do some calculation...\n")

time.sleep(3)

for i in range(0, 4):
    for j in range(0, 4):
        if list_A[i] + list_B[j] == 20:
            print("TRUE")
            exit()

print("FALSE")
```
**Testing the code**

![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Quizzes/Images/Quiz%20002%20-%20testing%20the%20code.png)

### Flow diagram
![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Quizzes/Images/Quiz%20002%20-%20Flow%20diagram%20-%201.JPG)
![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Quizzes/Images/Quiz%20002%20-%20Flow%20diagram%20-%202.JPG)
