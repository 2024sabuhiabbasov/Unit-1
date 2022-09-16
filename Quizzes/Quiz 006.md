## Quiz 005
**Statement**

Given a string, create a program that produces the sum of the characters in the string.

**My code**
```.py
str = input()
SumOfCharacters = 0

for i in range(0, len(str)):
    SumOfCharacters += (ord(str[i].lower()) - 96)

print(SumOfCharacters)
```

**Test**

![](https://raw.githubusercontent.com/2024sabuhiabbasov/Unit-1/main/Quizzes/Images/Quiz%20006.png)
