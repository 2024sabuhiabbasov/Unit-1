# Crypto Wallet application
import csv
import time # Importing time library to add breaks between operations
import json
import requests
from datetime import date
from my_library import validate_int_input
# Line above: Importing validate_int_input function from my_library.py to validate inputs
from my_library import password_check
from my_library import simple_login
from my_library import userName
from my_library import LastName
from my_library import account_date
from my_library import BNBconverter
from forex_python.converter import CurrencyRates

colors = ["\033[0;30m", "\033[0;31m", "\033[0;32m", "\033[0;33m", "\033[0;34m", "\033[0;35m", "\033[0;36m", "\033[0;37m"]
# Line above: Each element of the list colors[] represent a color as follows: black, red, green, yellow, blue, purple, cyan, white
bold_colors = ["\033[1;30m", "\033[1;31m", "\033[1;32m", "\033[1;33m", "\033[1;34m", "\033[1;35m", "\033[1;36m", "\033[1;37m"]
# Line above: Each element of the list colors[] represent a color but bold as follows: black, red, green, yellow, blue, purple, cyan, white
end_code = "\033[00m" # We need to use this variable to stop using formatting text (coloring in this code)

# New user registration
print(bold_colors[3] + "Welcome to Crypto Wallet Application!".center(146, ' ') + end_code)
print("\n", end='')
time.sleep(0.5) # waiting for 0.5 seconds
print(colors[3] + "Crypto Wallet app helps its users to follow their daily transactions in an easy way. We allow our users to add their transactions to and save".center(146, ' '))
time.sleep(0.2) # waiting for 0.2 seconds
print("in their account. Our users can see their purchases' amount in cryptocurrency BNB and USD, EURO, and YEN. They can also sort their transactions".center(146, ' '))
time.sleep(0.2) # waiting for 0.2 seconds
print("by category and month of purchase. We also care about our customers' privacy. All data received by the app are encrypted and can only be reached".center(146, ' '))
time.sleep(0.2) # waiting for 0.2 seconds
print("by the users themselves. We have created the app with a hope that our customers will enjoy while using it.".center(146, ' ') + end_code)
time.sleep(0.3) # waiting for 0.3 seconds
print(bold_colors[1] + "Stay with Crypto Wallet! ❤️".center(146, ' ') + end_code)
time.sleep(0.2) # waiting for 0.2 seconds
print(f"{bold_colors[1]}Note:{end_code} {colors[2]}Please keep in your mind that if you enter exit or finish in any input that you need to enter string, you will sign out from the program.{end_code}")
print(colors[3] + "\nWhat do you want to do?" + end_code)
time.sleep(0.1) # waiting for 0.1 seconds
option = """1. Log in
2. Sign up
"""
time.sleep(0.1) # waiting for 0.1 seconds
userID = validate_int_input(colors[2] + option + end_code + colors[3] + "\nPlease enter an option between 1 and 2 to continue: " + end_code)

while userID > 2 or userID < 1:
    userID = validate_int_input(bold_colors[1] + str(userID) + " is an incorrect option. Please enter an option between 1 and 2: " + end_code)
# Line above: while the user doesn't enter a valid number, it continues to ask

if userID == 2:
    name = input(colors[3] + "Please enter your name: ")
    if name == "exit" or name == "finish":
        print('\n')
        print(colors[2] + "You signed out successfully. Please come back soon ❤️".center(146, ' ') + end_code)
    surname = input("Please enter your surname: ")
    if surname == "exit" or surname == "finish":
        print('\n')
        print(colors[2] + "You signed out successfully. Please come back soon ❤️".center(146, ' ') + end_code)
    username = input("Please enter a username which you will use to log in: " + end_code)
    if username == "exit" or username == "finish":
        print('\n')
        print(colors[2] + "You signed out successfully. Please come back soon ❤️".center(146, ' ') + end_code)
    time.sleep(0.2) # waiting for 0.2 seconds
    print(f"{colors[2]}Conditions for a valid password:{end_code}{bold_colors[1]}")
    time.sleep(0.1) # waiting for 0.1 seconds
    print(f"✔️Must have at least one number.")
    time.sleep(0.1) # waiting for 0.1 seconds
    print(f"✔️Must have at least one uppercase and one lowercase character.")
    time.sleep(0.1) # waiting for 0.1 seconds
    print(f"✔️Must have at least one special symbol.")
    time.sleep(0.1) # waiting for 0.1 seconds
    print(f"✔️Must be between 6 to 20 characters long.{end_code}")
    time.sleep(0.1) # waiting for 0.1 seconds
    password = input(colors[3] + "Please choose a password: " + end_code)
    if password == "exit" or password == "finish":
        print('\n')
        print(colors[2] + "You signed out successfully. Please come back soon ❤️".center(146, ' ') + end_code)
    print(bold_colors[1])
    while password_check(password) != True:
        print(colors[3])
        password = input("Please input a valid password: ")
        if password == "exit" or password == "finish":
            print('\n')
            print(colors[2] + "You signed out successfully. Please come back soon ❤️".center(146, ' ') + end_code)
    passConf = input(end_code + colors[3] + "Please enter the password again to complete the registration: " + end_code)
    if passConf == "exit" or passConf == "finish":
        print('\n')
        print(colors[2] + "You signed out successfully. Please come back soon ❤️".center(146, ' ') + end_code)
    print(bold_colors[1])
    while password_check(passConf) != True:
        print(colors[3])
        passConf = input("Please input a valid password: " + end_code)
        if passConf == "exit" or passConf == "finish":
            print('\n')
            print(colors[2] + "You signed out successfully. Please come back soon ❤️".center(146, ' ') + end_code)
    print(end_code, end='')

    while password != passConf:
        print(bold_colors[1] + "Passwords don't match, " + end_code, end='')
        password = input(colors[3] + "please enter again: " + end_code)
        if password == "exit" or password == "finish":
            print('\n')
            print(colors[2] + "You signed out successfully. Please come back soon ❤️".center(146, ' ') + end_code)
        passConf = input(colors[3] + "Please enter again to complete the registration: " + end_code)
        if passConf == "exit" or passConf == "finish":
            print('\n')
            print(colors[2] + "You signed out successfully. Please come back soon ❤️".center(146, ' ') + end_code)
    if password == passConf:
        data = open('users.csv', 'a')
        data.write(f"{username},{password},{name},{surname},{date.today()}\n")
        data.close()
    print(f"{colors[3]}Registration successful.{bold_colors[2]} {name}{end_code}{colors[3]}, welcome to Crypto Wallet where you can see your transactions by one click!".center(176, ' '), end='')
    checker = True
    print(end_code + '\n')

elif userID == 1:
    username = input(colors[3] + "Please enter username to continue: ")
    if username == "exit" or username == "finish":
        print('\n')
        print(colors[2] + "You signed out successfully. Please come back soon ❤️".center(146, ' ') + end_code)
    password = input("Please enter password to login: " + end_code)
    if password == "exit" or password == "finish":
        print('\n')
        print(colors[2] + "You signed out successfully. Please come back soon ❤️".center(146, ' ') + end_code)
    checker = simple_login(username, password)
    while not checker:
        print(bold_colors[1] + "Wrong username or password. Please try again!" + end_code)
        username = input(colors[3] + "Please enter username again to continue: ")
        if username == "exit" or username == "finish":
            print('\n')
            print(colors[2] + "You signed out successfully. Please come back soon ❤️".center(146, ' ') + end_code)
        password = input("Please enter password again to login: " + end_code)
        if password == "exit" or password == "finish":
            print('\n')
            print(colors[2] + "You signed out successfully. Please come back soon ❤️".center(146, ' ') + end_code)
        checker = simple_login(username, password)

    if checker:
        name = userName(username, password)
        print(f"{colors[3]}Login successful.{bold_colors[2]} {name}{end_code}{colors[3]}, welcome to Crypto Wallet where you can see your transactions by one click!".center(176, ' '), end='')
        print(end_code + '\n')

time.sleep(0.5) # waiting for 0.5 seconds

menu = f"""① {colors[2]}New operation{end_code}
② {colors[2]}Transaction history{end_code}
③ {colors[2]}Show transactions summary{end_code}
④ {colors[2]}Account{end_code}
⑤ {colors[2]}About{end_code}
⑥ {colors[2]}Quit{end_code}
"""

time.sleep(0.5) # waiting for 0.5 seconds

print(bold_colors[3] + "Menu".center(20) + end_code)
# Line above: center function helps us to print the text in the center of given line length (30 in this code)
print(menu)

time.sleep(0.5) # waiting for 0.5 seconds

option = validate_int_input(colors[3] + "Please enter an option between 1 and 6 to choose a menu: " + end_code)
# Line above: using the function validate_int_input, getting a number from the user to continue
while option > 6 or option < 1:
    option = validate_int_input(bold_colors[1] + str(option) + " is an incorrect option." + colors[3] + " Please enter an option between 1 and 6: " + end_code)
# Line above: while the user doesn't enter a valid number, continue to ask

checker = True
total_balance = 0
while checker == True:
    # Option 6
    if option == 6:
        print("\n")
        print(colors[2] + "You signed out successfully. Please come back soon ❤️".center(146, ' ') + end_code)
        exit()

    # Option 5
    if option == 5:
        print(colors[3] + "About the app".center(146) + end_code, end='')
        print(f"""
① {colors[2]}The electronic ledger is a text-based software (Runs in the Terminal).{end_code}
② {colors[2]}The electronic ledger display the basic description of the cryptocurrency selected.{end_code}
③ {colors[2]}The electronic ledger allows to enter, withdraw and record transactions.{end_code}
④ {colors[2]}The electronic ledger shows the values of datas in 3 currencies: US Dollar, Euro, Japanese Yen.{end_code}
⑤ {colors[2]}The application is protected with authentication questions.{end_code}
⑥ {colors[2]}The electronic ledger can categorize transactions done by the user. For example, how much crypto money spent on daily products.{end_code}
""")
        print(colors[3] + "About the currency".center(146) + end_code)
        print(colors[2] + "The electronic ledger is using the cryptocurrency BNB. BNB was initially based on the Ethereum network but is now ".center(146))
        print("the native currency of Binance's own blockchain, the Binance chain. Its uses have expanded to numerous applications ".center(146))
        print("on a wide number of platforms. It is used to pay for transaction fees on Binance.com, Binance DEX, and Binance Chain.".center(146) + end_code)

    # Option 1
    if option == 1:
        print(end_code)
        option1menu = f'''{end_code}① {colors[2]}Spending{end_code}
② {colors[2]}Top-up balance{end_code}
'''
        print(colors[2] + option1menu + end_code)

        time.sleep(0.5) # waiting for 0.5 seconds

        option1 = validate_int_input(colors[3] + "Please enter an option between 1 and 2 to choose an operation: " + end_code)
        # Line above: using the function validate_int_input, getting a number from the user to continue
        while option1 > 2 or option1 < 1:
            option1 = validate_int_input(bold_colors[1] + str(option1) + " is an incorrect option." + colors[3] + " Please enter an option between 1 and 2: " + end_code)
        # Line above: while the user doesn't enter a valid number, continue to ask
        checker2 = True
        while checker2:
            # Option 2.1
            if option1 == 1:
                categories_list =f"""
{bold_colors[3] + "Categories".center(25, ' ') + end_code}
🚗️ {colors[2]}Car
🍓️ Food
🍹️ Drink
🏠️ House
💡️ Other{end_code}

{colors[2]}If a category you type is not in the list, it will be saved in {colors[1]}Other{end_code} {colors[2]}category section.{end_code}
"""
                print(categories_list)
                spendingCategory = input(colors[3] + "Please enter the category of your purchase: ")
                if spendingCategory == "exit" or spendingCategory == "finish":
                    print('\n')
                    print(colors[2] + "You signed out successfully. Please come back soon ❤️".center(146, ' ') + end_code)
                spendingCategory = spendingCategory.title()
                categories_list1 = ['Car', 'Food', 'Drink', 'House', 'Other']
                if not spendingCategory in categories_list1:
                    spendingCategory = "Other"
                spendingAmount = validate_int_input(colors[3] + "Please enter the amount of BNB spent for the purchase: " + end_code)
                spendingAmountUSD = BNBconverter(spendingAmount)
                spendingDate = input(colors[3] + "Please enter the date of your purchase in the given YYYY-DD-MM format: " + end_code)
                if spendingDate == "exit" or spendingDate == "finish":
                    print('\n')
                    print(colors[2] + "You signed out successfully. Please come back soon ❤️".center(146, ' ') + end_code)
                time.sleep(0.1) # waiting for 0.1 seconds
                print(f"{bold_colors[2]}Successfully{end_code} {colors[3]}added to your transactions!{end_code}\n")
                time.sleep(0.1) # waiting for 0.1 seconds
                spendingData = open('spendings.csv', 'a')
                spendingData.write(f"{spendingCategory},{str(spendingAmount)},{str(int(spendingAmountUSD))},{spendingDate}\n")
                spendingData.close()
                next_step = input(f"{colors[3]}Do you want to add another purchase? If{end_code}{colors[3]} yes, please enter '{colors[2]}YES/yes/s{end_code}{colors[3]}.' If no, please enter '{colors[2]}NO/no/n{colors[3]}': {end_code}")
                if next_step == "exit" or next_step == "finish":
                    print('\n')
                    print(colors[2] + "You signed out successfully. Please come back soon ❤️".center(146, ' ') + end_code)
                if next_step.lower() == "yes" or next_step.lower() == 'y':
                    checker2 = True
                elif next_step.lower() == "no" or next_step.lower() == 'n':
                    checker2 = False
            # Option 1.2
            elif option1 == 2:
                checker3 = True
                while checker3:
                    deposit = validate_int_input(f"{colors[3]}Please input amount of BNB you want to add to your account: {colors[3]}")
                    total_balance += deposit
                    next_step = input(f"{colors[3]}Do you want to add another deposit? If{end_code}{colors[3]} yes, please enter '{colors[2]}YES/yes/y{end_code}{colors[3]}.' If no, please enter '{colors[2]}NO/no/n{colors[3]}': {end_code}")
                    if next_step == "exit" or next_step == "finish":
                        print('\n')
                        print(colors[2] + "You signed out successfully. Please come back soon ❤️".center(146, ' ') + end_code)
                    if next_step.lower() == "yes" or next_step.lower() == 'y':
                        checker3 = True
                    elif next_step.lower() == "no" or next_step.lower() == 'n':
                        checker3 = False
                break

    # Option 4
    if option == 4:
        print(f"{bold_colors[3]}Account{end_code}".center(146, ' '))
        name = userName(username, password)
        surname = LastName(username, password)
        account_creation_date = account_date(username, password)
        user_information = f"""
{colors[3]}Username:               {bold_colors[2]}{username}{end_code}
{colors[3]}First name:             {bold_colors[2]}{name}{end_code}
{colors[3]}Last name:              {bold_colors[2]}{surname}{end_code}
{colors[3]}Balance:                {bold_colors[2]}{total_balance}{end_code}
{colors[3]}Account creation date:  {bold_colors[2]}{account_creation_date}{end_code}
"""
        
        print(f"{user_information}")
    # Solve option 2
    if option == 2:
        # Adding the heading
        print(bold_colors[3] + "Transaction history".center(58, " ") + end_code)
        # Creating a value of 58 dashes for the table heading
        dashes = f"{bold_colors[6]}{'-'*58}{end_code}"
        # Printing the table's first line
        print(f"{dashes}")
        # Opening the spendings.csv file to get transactions data
        with open("spendings.csv") as file:
            database = file.readlines()
        dash = f"{colors[6]}|{end_code}"
        # Printing table titles in the second line of the table
        print(colors[6] + '|' + end_code + bold_colors[5] + "Category".center(18, ' ') + end_code, end='')
        print(colors[6] + '|' + end_code + bold_colors[5] + "Cost".center(19, ' ') + end_code, end='')
        print(colors[6] + '|' + end_code + bold_colors[5] + "Date".center(17, ' ') + end_code, end=dash)
        print('\n' + dashes)
        # Printing every line of transactions we have gotten from the file spendings.csv in the previous lines
        for line in database:
            line_cleaned = line.strip() # remove \n
            spending = line_cleaned.split(",") # splitting our datas from ','

            # Checking if the category is car, it prints all related data in red
            if spending[0] == "Car":
                # Printing the category of the transaction
                print(f"{colors[6]}|{end_code}{colors[1]}{spending[0].ljust(18, ' ')}{end_code}", end='')
                # Printing the value of purchase
                print(f"{colors[6]}|{end_code}{colors[1]}{spending[1].ljust(5, ' ')}{bold_colors[1]}{'BNB'.ljust(2)} {end_code}{colors[1]}{spending[2].ljust(7, ' ')}{bold_colors[1]}{'USD'.ljust(0)}{end_code}", end='')
                # Printing the date of the transaction
                print(f"{colors[6]}|{end_code}{colors[1]}{spending[3].ljust(17, ' ')}{end_code}", end=dash)
                print(f"\n{dashes}")

            # Checking if the category is house, it prints all related data in purple
            elif spending[0] == "House":
                # Printing the category of the transaction
                print(f"{colors[6]}|{end_code}{colors[5]}{spending[0].ljust(18, ' ')}{end_code}", end='')
                # Printing the value of purchase
                print(f"{colors[6]}|{end_code}{colors[5]}{spending[1].ljust(5, ' ')}{bold_colors[5]}{'BNB'.ljust(2)} {end_code}{colors[5]}{spending[2].ljust(7, ' ')}{bold_colors[5]}{'USD'.ljust(0)}{end_code}", end='')
                # Printing the date of the transaction
                print(f"{colors[6]}|{end_code}{colors[5]}{spending[3].ljust(17, ' ')}{end_code}", end=dash)
                print(f"\n{dashes}")

            # Checking if the category is food, it prints all related data in green
            elif spending[0] == "Food":
                # Printing the category of the transaction
                print(f"{colors[6]}|{end_code}{colors[2]}{spending[0].ljust(18, ' ')}{end_code}", end='')
                # Printing the value of purchase
                print(f"{colors[6]}|{end_code}{colors[2]}{spending[1].ljust(5, ' ')}{bold_colors[2]}{'BNB'.ljust(2)} {end_code}{colors[2]}{spending[2].ljust(7, ' ')}{bold_colors[2]}{'USD'.ljust(0)}{end_code}", end='')
                # Printing the date of the transaction
                print(f"{colors[6]}|{end_code}{colors[2]}{spending[3].ljust(17, ' ')}{end_code}", end=dash)
                print(f"\n{dashes}")

            # Checking if the category is car, it prints all related data in blue
            elif spending[0] == "Drink":
                # Printing the category of the transaction
                print(f"{colors[6]}|{end_code}{colors[4]}{spending[0].ljust(18, ' ')}{end_code}", end='')
                # Printing the value of purchase
                print(f"{colors[6]}|{end_code}{colors[4]}{spending[1].ljust(5, ' ')}{bold_colors[4]}{'BNB'.ljust(2)} {end_code}{colors[4]}{spending[2].ljust(7, ' ')}{bold_colors[4]}{'USD'.ljust(0)}{end_code}", end='')
                # Printing the date of the transaction
                print(f"{colors[6]}|{end_code}{colors[4]}{spending[3].ljust(17, ' ')}{end_code}", end=dash)
                print(f"\n{dashes}")

            # Checking if the category is car, it prints all related data in yellow
            elif spending[0] == "Other":
                # Printing the category of the transaction
                print(f"{colors[6]}|{end_code}{colors[3]}{spending[0].ljust(18, ' ')}{end_code}", end='')
                # Printing the value of purchase
                print(f"{colors[6]}|{end_code}{colors[3]}{spending[1].ljust(5, ' ')}{bold_colors[3]}{'BNB'.ljust(2)} {end_code}{colors[3]}{spending[2].ljust(7, ' ')}{bold_colors[3]}{'USD'.ljust(0)}{end_code}", end='')
                # Printing the date of the transaction
                print(f"{colors[6]}|{end_code}{colors[3]}{spending[3].ljust(17, ' ')}{end_code}", end=dash)
                print(f"\n{dashes}")

    # Option 3
    if option == 3:
        with open("spendings.csv") as file:
            database = file.readlines()
            categories = ["Food", "Car", "House", "Drink", "Other"]
            totals = [0, 0, 0, 0, 0]
            for line in database:
                line_cleaned = line.strip() # remove \n
                spending = line_cleaned.split(",")
                cat = spending[0]
                value = spending[1]
                if cat == categories[0]:
                    totals[0] += int(value)
                elif cat == categories[1]:
                    totals[1] += int(value)
                elif cat == categories[2]:
                    totals[2] += int(value)
                elif cat == categories[3]:
                    totals[3] += int(value)
                elif cat == categories[4]:
                    totals[4] += int(value)
            print(bold_colors[3] + "Transactions summary".center(44, ' ') + end_code)
            print(f"{colors[2]}{categories[0].upper().ljust(10)}{('■'*(totals[0]//10)).ljust(30)}{colors[2]}{totals[0]}")
            print(f"{colors[1]}{categories[1].upper().ljust(10)}{('■'*(totals[1]//10)).ljust(30)}{colors[1]}{totals[1]}")
            print(f"{colors[5]}{categories[2].upper().ljust(10)}{('■'*(totals[2]//10)).ljust(30)}{colors[5]}{totals[2]}")
            print(f"{colors[4]}{categories[3].upper().ljust(10)}{('■'*(totals[3]//10)).ljust(30)}{colors[4]}{totals[3]}")
            print(f"{colors[3]}{categories[4].upper().ljust(10)}{('■'*(totals[4]//10)).ljust(30)}{colors[3]}{totals[4]}{end_code}")
            print(f"{bold_colors[1]}Note:{end_code} {colors[2]}Please keep in your mind that one square represents {bold_colors[1]}10 BNB{colors[2]}{end_code}")

    # Line below: asking the user if they want to continue
    next_step = input(f"{colors[3]}Do you want to continue to use the app? If{end_code}{colors[3]} yes, please enter '{colors[2]}YES/yes/y{end_code}{colors[3]}.' If no, please enter '{colors[2]}NO/no/n{colors[3]}': {end_code}")
    if next_step.lower() == "yes" or next_step.lower() == 'y':
        menu = f"""{end_code}① {colors[2]}New operation{end_code}
② {colors[2]}Transaction history{end_code}
③ {colors[2]}Show transactions summary{end_code}
④ {colors[2]}Account{end_code}
⑤ {colors[2]}About{end_code}
⑥ {colors[2]}Quit{end_code}
"""
        print(colors[3] + "Menu".center(30) + end_code)
        print(colors[2] + menu + end_code)
        checker = True
        option = validate_int_input(colors[2] + "Please enter an option between 1 and 6: " + end_code)
    elif next_step.lower() == "no" or next_step.lower() == 'n':
        checker = False
        print('\n')
        print(colors[2] + "You signed out successfully. Please come back soon ❤️".center(146, ' ') + end_code)
        exit()
