# Quiz 015
**Statement**

There are N closed doors in a school and N students present. The first student opens each door. The second student flips (open⇆close) every second door. The third student flips every third door, and so on. 

[SL]Create a function that shows the doors after 5 students.
[HL]Create a function that shows the doors open after N students.

## Test cases
![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Quizzes/Images/Quiz%20015%20-%20test%20cases.png)

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
        num = input(f"{red}{prompt}{end_code}")

    return int(num)

def open_doors(numberOfStudents: int):
    doors = []

    for i in range(0, numberOfStudents):
        doors.append(False)

    for i in range(1, numberOfStudents + 1):
        for j in range(1, numberOfStudents + 1):
            if i % j == 0:
                doors[i - 1] = not doors[i - 1]
    #i = 1
    #cnt = 0
    #while i * i <= n:
    #    cnt += 1

    #print(cnt)

    print("Doors: ", end='')

    for i in range(0, numberOfStudents):
        if doors[i]:
            print('O', end='')
        elif not doors[i]:
            print('C', end='')
        if i != n - 1:
            print(', ', end='')


n = validate_int_input("Please enter the number of students N and the number of open doors N: ")
open_doors(numberOfStudents=n)
```
### Flow diagram
![]()

**Testing the code**

**Test 1**

![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Quizzes/Images/Quiz%20015%20-%20testing%20the%20program.png)
