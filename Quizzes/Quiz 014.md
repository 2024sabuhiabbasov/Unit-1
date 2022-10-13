# Quiz 014
**Statement**

Create a function that receives one input and produces the output shown. 

## Test cases
![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Quizzes/Images/Quiz%20014%20-%20test%20cases.png)

## My solutions
### Code
```.py
def validate_int_input(prompt:str)->int:
    '''
    This function asks the user for an input and validates
    that the input is an integer
    returns: integer
    '''

    end_code = "\033[00m"
    red = "\033[0;31m"
    num = input(prompt)
    while not num.isdigit():
        num = input(f"{red}Wrong input!{end_code} {prompt}{end_code}")

    return int(num)

def mysteryTwo(a: int, b: int)-> int:
    return ((a**2) + b)

a = validate_int_input("Please enter a: ")
b = validate_int_input("Please enter b: ")

answer = mysteryTwo(a, b)

print(answer)
```
### Flow diagram
![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Quizzes/Images/Quiz%20014%20-%20Flow%20diagram.jpg)

**Testing the code**

**Test 1**

![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Quizzes/Images/Quiz%20014%20-%20testing%20the%20program.png)
