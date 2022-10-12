# Quiz 012
**Statement**

Create a function that receives integer 2<N<10, and returns the multiplication table for the number up to 9. [HL] Users input any month.

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
        num = input(f"{red}Error {prompt}{end_code}")

    return int(num)

def mulTable(number: int)->str:
    multiplication_table = ''
    for i in range(1, 10):
        multiplication_table += str(number) + ' x ' + str(i) + ' = ' + str(number * i) + '\n'
    return multiplication_table

end_code = "\033[00m"
colors = ['\33[0;30m', '\33[0;31m', '\33[0;32m', '\33[0;33m', '\33[0;34m', '\33[0;35m', '\33[0;36m']

number = validate_int_input("Please input a number which you want to multiply with from 1 to 9: ")

print(colors[2] + "Multiplication table".center(40, ' ') + '\n' + mulTable(number) + end_code)
```
### Flow diagram
![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Quizzes/Images/Quiz%20012%20-%20Flow%20diagram.jpg)

**Testing the code**

**Test 1**

![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Quizzes/Images/Quiz%20012%20-%20testing%20the%20program.png)
