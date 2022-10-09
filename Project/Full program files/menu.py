# Program for menu of Crypto Wallet
import time # Importing time library to add breaks between operations
from my_library import validate_int_input
# Line above: Importing validate_int_input function from my_library.py to validate inputs

colors = ["\033[0;30m", "\033[0;31m", "\033[0;32m", "\033[0;33m", "\033[0;34m"]
# Line above: Each element of the list colors[] represent a color as follows: black, red, green, yellow, blue
end_code = "\033[00m" # We need to use this variable to stop using formatting text (coloring in this code)

intro_msg = colors[2] + "Welcome to Crypto Wallet where you can see your transactions by one click!\n" + end_code
print(intro_msg)

time.sleep(0.5) # waiting for 0.5 seconds

menu = """1. New operation
2. Transaction history
3. Account
4. About
5. Quit
"""

time.sleep(0.5) # waiting for 0.5 seconds

print(colors[3] + "Menu".center(30) + end_code)
# Line above: center function helps us to print the text in the center of given line length (30 in this code)
print(colors[2] + menu + end_code)

time.sleep(0.5) # waiting for 0.5 seconds

option = validate_int_input("Please enter an option between 1 and 5: ")
# Line above: using the function validate_int_input, getting a number from the user to continue
while option > 5 or option < 1:
    option = validate_int_input(colors[1] + str(option) + " is an incorrect option. Please enter an option between 1 and 5: " + end_code)
# Line above: while the user doesn't enter a valid number, continue to ask

checker = True

while checker == True:
    # Option 5
    if option == 5:
        print(colors[4] + "You signed out successfully, see you again!" + end_code)
        exit()

    # Option 4
    if option == 4:
        print(colors[3] + "About".center(30) + end_code, end='')
        print(colors[2] + """
1. The electronic ledger is a text-based software (Runs in the Terminal).
2. The electronic ledger display the basic description of the cryptocurrency selected.
3. The electronic ledger allows to enter, withdraw and record transactions.
4. The electronic ledger shows the values of datas in 3 currencies: US Dollar, Euro, Japanese Yen.
5. The application is protected with authentication questions.
6. The electronic ledger can categorize transactions done by the user. For example, how much crypto money spent on daily products.
        """ + end_code)

    # Option 2
    if option == 2:
        print(colors[2] +  + end_code)

    # Option 3
    if option == 3:
        print(colors[2] + + end_code)

    # Solve option 1
    if option == 1:
        print(colors[2] + + end_code)

    # Line below: asking the user if they want to continue
    next_step = input(colors[1] + "Do you want to continue? If yes, please enter 'YES.' If no, please enter 'NO' " + end_code)
    if next_step == 'YES' or next_step == "yes":
        menu = """1. New operation
2. Transaction history
3. Account
4. About
5. Quit
"""
        print(colors[3] + "Menu".center(30) + end_code)
        print(colors[2] + menu + end_code)
        checker = True
        option = validate_int_input(colors[2] + "Please enter an option between 1 and 5: " + end_code)
    elif next_step == 'NO' or next_step == "no":
        checker = False
        print(colors[3] + "We are sorry to see you go..." + end_code)
