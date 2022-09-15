## Quiz 007
**Statement**

Create a program that creates 10 random password with digits and letters of length 20. If you are an HL student, ask the user for the length and if symbols should be included. Print answer in RED.

**My code**
```.py
import random

length = int(input("Please input the length of the password: "))
symbol = input("Do you want to use symbols in your password? If yes, please enter TRUE. If no, please enter FALSE: ")

for j in range(0, 10):
    print("Password №" + str(j + 1) + ": " , end ="")
    for i in range(0, length):
        n = random.randint(48, 122)
        if symbol == 'FALSE' or symbol == 'false':
            while (not(n >= 48 and n <= 57) and not(n >= 97 and n <= 122)) and not(n >= 65 and n <= 90):
                n = random.randint(48, 122)
            print("\33[0;31m" + chr(n) + "\033[00m", end ="")
        elif symbol == 'TRUE' or symbol == 'true':
            n = random.randint(48, 122)
            print("\33[0;31m" + chr(n) + "\033[00m", end ="")
    print("\n")
```
**Test**
![](https://raw.githubusercontent.com/2024sabuhiabbasov/Unit-1/main/Quizzes/Images/Quiz%20007.png)
