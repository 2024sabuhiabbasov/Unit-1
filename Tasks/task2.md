# Task 2

**Statement**

Make a program for the EV calculator

------ Welcome to EV Calculator-------

   Options
1. Average time per kWh
2. Total kWh used
3. Total charge time
4. Show all data

## My solution
### Code
```.py
# Task 2
import time
from my_library import validate_int_input

colors = ["\033[0;30m", "\033[0;31m", "\033[0;32m", "\033[0;33m", "\033[0;34m"]
end_code = "\033[00m"

intro_msg = colors[2] + "Welcome to EV Calculator" + end_code
print(intro_msg.center(50))

time.sleep(1)


menu = """1. Average time per kWh
2. Total kWh used
3. Total charge time
4. Show all data
"""
time.sleep(1)

print(colors[2] + "Options".center(50) + end_code)
print(colors[2] + menu + end_code)

time.sleep(1)

option = validate_int_input(colors[2] + "Please enter an option [1-4]: " + end_code)
while option > 4 or option < 1:
    option = validate_int_input(colors[1] + str(option) + " is an incorrect option. Please enter an option [1-4]: " + end_code)

# This is how to read a file
with open("charging_log.csv", "r") as file:
    ev_data = file.readlines()

checker = True

while checker == True:
    # Solve option 4
    if option == 4:
        cnt = -1
        for line in ev_data:
            cnt += 1
            # Strip removes the \n from the string
            line = line.strip()
            if cnt != 0:
                print(colors[2] + "Log №" + str(cnt) + ": " + end_code, end='')
            print(colors[2] + line + end_code)

    #Solve option 2
    elif option == 2:
        total_energy = 0
        cnt = 0
        for line in ev_data:
            if cnt > 0:
                values = line.split(',')
                charge = values[1]
                charge_cleaned = charge[:5]
                charge_float = float(charge_cleaned)
                total_energy += charge_float

            cnt += 1
        print(colors[2] + "The total energy used is " + str(total_energy) + "kWh.\n" + end_code)

    # Solve option 3
    elif option == 3:
        total_time = 0
        cnt = 0
        for line in ev_data:
            if cnt > 0:
                values = line.split(',')
                time = values[2]
                time = time.split(':')
                total_time += (int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2]))
            cnt += 1
        print(colors[2] + "Total charge time is " + str(total_time // 3600) + ':' + str(total_time//60 % 60) + ':' + str(total_time % 60) + '.\n' + end_code)

    # Solve option 1
    elif option == 1:
        total_energy = 0
        total_time = 0
        cnt = 0
        for line in ev_data:
            if cnt > 0:
                values = line.split(',')
                charge = values[1]
                charge_cleaned = charge[:5]
                charge_float = float(charge_cleaned)
                total_energy += charge_float
                time = values[2]
                time = time.split(':')
                total_time += (int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2]))
            cnt += 1
        average_energy = int(total_time / total_energy)
        print(colors[2] + "Average time per kWh per hour is " + str(average_energy // 3600) + ':' + str(average_energy//60 % 60) + ':' + str(average_energy % 60) + '.\n' + end_code)

    menu = """1. Average time per kWh
2. Total kWh used
3. Total charge time
4. Show all data
"""

    print(colors[2] + "Options".center(50) + end_code)
    print(colors[2] + menu + end_code)
    next_step = input(colors[1] + "Do you want to continue? If yes, please enter 'YES.' If no, please enter 'NO' " + end_code)
    if next_step.upper() == 'YES':
        checker = True
        option = validate_int_input(colors[2] + "Please enter an option [1-4]: " + end_code)
    elif next_step.upper() == 'NO':
        checker = False
        print(colors[2] + "Goodbye!" + end_code)
```

### Testing the code
![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Tasks/Images/Task%202%20-%20testing%20the%20program%200.png)
![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Tasks/Images/Task%202%20-%20testing%20the%20program%201.png)
