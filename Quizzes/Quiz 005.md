## Quiz 005
**Statement**

Create a program that translate the proteins in the DNA chain as shown below. [HL]  Input is a whole protein chain as a string.

**My code**
```.py
## Quiz 003
**Statement**
Given a number, create a program that produces the output factors.

**Example**
![](https://raw.githubusercontent.com/2024sabuhiabbasov/Unit-1/main/Quizzes/Images/Quiz%20003%20-%20test.png)

**My code**
```.py
# Program to find the factors of a number

def factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x//2):
       if x % i == 0:
           print(i)

num = int(input("Please enter a number to see its factors: "))

factors(num)
print(num)
```

**Test**

![](https://raw.githubusercontent.com/2024sabuhiabbasov/Unit-1/main/Quizzes/Images/Quiz%20005.png)
