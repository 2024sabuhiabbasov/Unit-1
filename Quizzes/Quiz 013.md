# Quiz 013
**Statement**

Create a function that receives one input and produces the output shown. 

## Test cases
![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Quizzes/Images/Quiz%20013%20-%20test%20cases.png)

## My solutions
### Code
```.py
def mystery(a: int, b: int)->int:
    if a != b:
        return a * b - abs(a - b)
    else:
        return a * b - a


a = int(input("Please enter a: "))
b = int(input("Please enter b: "))

answer = mystery(a, b)

print("This is the answer: " + answer)
```
### Flow diagram
![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Quizzes/Images/Quiz%20013%20-%20Flow%20diagram.jpg)

**Testing the code**

**Test 1**

![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Quizzes/Images/Quiz%20013%20-%20testing%20the%20program.png)
