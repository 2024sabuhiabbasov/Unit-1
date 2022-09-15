## Quiz 007
**Statement**

Create a program that creates 10 random password with digits and letters of length 20. If you are an HL student, ask the user for the length and if symbols should be included. Print answer in RED.

**My code**
```.py
import random

length = int(input("Please input the length of the password: "))
symbol = input("Do you want to use symbols in your password? If yes, please enter TRUE. If no, please enter FALSE: ")

for j in range(0, 10):
    print("Password №" + str(j) + ": " , end ="")
    for i in range(0, length):
        n = random.randint(48, 122)
        if symbol == 'FALSE':
            while (not(n >= 48 and n <= 57) and not(n >= 97 and n <= 122)) and not(n >= 65 and n <= 90):
                n = random.randint(48, 122)
            print(chr(n), end ="")
        elif symbol == 'TRUE':
            n = random.randint(48, 122)
            print(chr(n), end ="")
    print("\n")
```
