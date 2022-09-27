# Quiz 009
**Statement**

Create a function that receives as input a string and returns the string ciphered with shift 13. [HL]  Ask the user for the shift.

**Test cases**

![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Quizzes/Images/Quiz%20009%20-%20test%20cases.png)

## My solutions
### Code
```.py
import string

alphabet_string = (string.ascii_lowercase + string.ascii_uppercase) * 100
alphabet_list = list(alphabet_string)

colors = ["\033[0;30m", "\033[0;31m", "\033[0;32m", "\033[0;33m", "\033[0;34m"]
end_code = "\033[00m"

str = input("Please enter a text whose characters you want to shift: ")
length = len(str)

shift = input("\nThanks! Please input how many characters you want to shift: ")

for i in range(0, length):
    if str[i] in alphabet_list:
        if str[i].isupper():
            index = alphabet_list.index(str[i])
            print(alphabet_list[index + int(shift)].upper(), end='')
        else:
            index = alphabet_list.index(str[i])
            print(alphabet_list[index + int(shift)].lower(), end='')
    else:
        print(str[i], end='')
```
### Flow diagram

![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Quizzes/Images/Quiz%20009%20-%20flow%20diagram.jpg)

**Testing the code**

**Test 1**

![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Quizzes/Images/Quiz%20009%20-%20testing%20the%20code%20(1).png)

**Test 2**

![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Quizzes/Images/Quiz%20009%20-%20testing%20the%20code%20(2).png)

**Test 3**

![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Quizzes/Images/Quiz%20009%20-%20testing%20the%20code%20(3).png)
