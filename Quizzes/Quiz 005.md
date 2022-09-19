# Quiz 005
**Statement**

Given a number, create a program that produces the output factors.

**Test cases**

![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Quizzes/Images/Quiz%20005%20-%20test%20cases.png)

## My solutions
###Code
```.py# Program to find the factors of a number

def factors(x):
   sum = 0
   counter = 0
   print("The factors of",x,"are:")
   for i in range(1, x):
       if x % i == 0:
           sum += i
           counter += 1
           print("Factor №" + str(counter) + ": " + str(i))
           if sum == x:
               print("The sum of factors is equal to", str(x))

num = int(input("Please enter a number to see its factors: "))

factors(num)
```

**Testing the code**

![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Quizzes/Images/Quiz%20005%20-%20testing%20the%20code%20-%201.png)

### Flow diagram

![]()
