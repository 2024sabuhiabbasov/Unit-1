## Quiz 005
**Statement**

Given a number, create a program that produces the output factors.

**Test cases**

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
