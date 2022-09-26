# Quiz 011
**Statement**

Create a function that shows the days of your birthday’s month for the year 2022. [HL]  Users input any month.

**Test cases**

![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Quizzes/Images/Quiz%20011%20-test%20cases.png)

## My solutions
### Code
```.py
def bestMonth()->str:

    end_code = "\033[00m"
    colors = ['\33[0;30m', '\33[0;31m', '\33[0;32m', '\33[0;33m', '\33[0;34m', '\33[0;35m', '\33[0;36m']
    birthdayMonth = "June 2022"
    print(colors[2] + "The names of days in", birthdayMonth + ':' + end_code, end='\n\n')
    weekDays = ["We", "Th", "Fr", "Sa", "Su", "Mo", "Tu"]
    for i in range(1, 31):
        if i % 7 == 1:
            print(colors[1] + weekDays[0] + end_code, end=' ')
        elif i % 7 == 2:
            print(colors[1] + weekDays[1] + end_code, end=' ')
        elif i % 7 == 3:
            print(colors[1] + weekDays[2] + end_code, end=' ')
        elif i % 7 == 4:
            print(colors[1] + weekDays[3] + end_code, end=' ')
        elif i % 7 == 5:
            print(colors[1] + weekDays[4] + end_code, end=' ')
        elif i % 7 == 6:
            print(colors[1] + weekDays[5] + end_code, end=' ')
        elif i % 7 == 0:
            print(colors[1] + weekDays[6] + end_code, end=' ')
        print(colors[2] + str(i) + end_code, end='')
        if not i == 30:
            print(',', end=' ')
        if i % 15 == 0 and not i == 30:
            print("\n")

bestMonth()
```

**Testing the code**

**Test 1**

![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Quizzes/Images/Quiz%20011%20-%20testing%20the%20code.png)
