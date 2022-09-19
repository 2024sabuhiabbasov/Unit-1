# Quiz 006
**Statement**

Given a string, create a program that produces the sum of the characters in the string.

**Test cases**

![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Quizzes/Images/Quiz%20006%20-%20test%20cases.png)

## My solutions
### Code
```.py
str = input()
SumOfCharacters = 0

for i in range(0, len(str)):
    SumOfCharacters += (ord(str[i].lower()) - 96)

print(SumOfCharacters)
```

**Testing the code**

![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Quizzes/Images/Quiz%20006%20-%20testing%20the%20code.png)

### Flow diagram

![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Quizzes/Images/Quiz%206%20-%20Flow%20diagram.JPG)
