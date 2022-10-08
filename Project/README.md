# Crypto Wallet

![](https://github.com/drPinzonISAK/unit1_g1/blob/main/22ROOSE-master768.gif)  
<sub>Illustration for Glenn Harvey</sub>

# Criteria A: Planning

## Problem definition

Ms. Sato is a local trader who is interested in the emerging market of cryptocurrencies. She has started to buy and sell electronic currencies, however at the moment she is tracking all his transaction using a ledger in a spreadsheet which is starting to become burdensome and too disorganized. It is also difficult for Ms Sato to find past transactions or important statistics about the currency. Ms Sato is in need of a digital ledger that helps her track the amount of the cryptocurrency, the transactions, along with useful statistics. 

Apart for this requirements, Ms Sato is open to explore a cryptocurrency selected by the developer.

## Proposed Solution

Design statement:
I will to design and make a CryptoWallet for a client who is a local trader in Japan. The CryptoWallet app is constructed using the software Python. It will take  1 month to make and will be evaluated according to the criteria A.

I am going to use the cryptocurrency named **BNB**. BNB was initially based on the Ethereum network but is now the native currency of Binance's own blockchain, the Binance chain. Its uses have expanded to numerous applications on a wide number of platforms. It is used to pay for transaction fees on Binance.com, Binance DEX, and Binance Chain.

(Resource: https://www.investopedia.com/terms/b/binance-coin-bnb.asp)

Justify the tools/structure of your solution

## Success Criteria
1. The electronic ledger is a text-based software (Runs in the Terminal).
2. The electronic ledger display the basic description of the cryptocurrency selected.
3. The electronic ledger allows to enter, withdraw and record transactions.
4. The electronic ledger shows the values of datas in 3 currencies: US Dollar, Euro, Japanese Yen. 
5. The application is protected with authentication questions.
6. The electronic ledger can categorize transactions done by the user. For example, how much crypto money spent on daily products.

# Criteria B: Design

## System Diagram
![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Project/Images/Unit%201%20Project%20-%20System%20Diagram.jpg)

The program will be based on Windows 10 with AMD Ryzen 3 3250U processor with 8 GB of RAM. The program will be written in the Python language. I will use PyCharm 2022.1.3 version to implement my ideas to code. There will be reading and writing operations between database.csv and CryptoWallet.py file. My program will get input by using the keyboard and print the output by using the monitor.

## Flow Diagrams
### Login system
Login systems uses the users.csv to check if the entered username and pssword match in the data written in users.csv. If yes, the user can enter to her account. If no, she needs to enter the login details again.
![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Project/Images/Login%20system%20-%20Flow%20Diagram.jpg)

### Password check
To protect the customer's privacy, my program checks if the customer chooces a strong password for login. The customer is asked to reenter the password unless she enters a valid password. Also, she is given special instructions about password choose based on the password she has entered.
![]()

### BNBConverter
To read the data in an eaiser way, the program prints BNB values in USD as well. This is the flow diagram of converting BNB to USD.
![]()

## Record of Tasks
| Task No | Planned Action                                               | Planned Outcome                                                                                                 | Time estimate | Target completion date | Criteria | Status |
|---------|---------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|---------------|------------------------|-----------|-----------|
| 1 | Create [system diagram](https://github.com/2024sabuhiabbasov/Unit-1/edit/main/Project/README.md#system-diagram) | To have a clear idea of the hardware and software requirements for the proposed solution | 10min | Sep 23 | B | Completed |
| 2 | Complete [Success Criteria](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Project/README.md#success-criteria) | To have criteria that meet the buyer's expectations | 15 mins | Sep 23 | A | Completed |
| 3 | Create a login system | A coded and tested login system to protect the application with username and password | 30 mins | Sep 29 | C | Completed |
| 4 | Create a [flow diagram for login system](https://github.com/2024sabuhiabbasov/Unit-1/tree/main/Project#login-system) | To make it easier for the customer to know how the login system works | 20 mins | Sep 30 | B | Completed |
| 5 | Create a menu | To have a coded and tested menu to welcome the customer and make it easy for her to navigate between menus | 30 mins | Oct 2 | C | Completed |
| 6 | Customer test | To have a feedback from a real customer after the cusotomer's app usage | 10 mins | Oct 7 | E | Completed |
| 7 | Updating text formatting | To have an updated text format to make the app more more clear for the customer based on feedback from the customer meeting | 2 hours | Oct 7 | C | Completed |
| 8 | Adding online currency resource | To have a coded and tested online currency converter in the app to convert money between BNB and USD | 1 hour | Oct 8 | C | Completed |
| 9 | Testing the program | To have an idea of how the user will be welcomed and the app will work and adding improvements based on those ideas | 30 mins | Oct 8 | C and E | Completed |

# Criteria C: Development

## Password validation
To protect the customer's privacy, my program checks if the customer chooces a strong password for login. The customer is asked to reenter the password unless she enters a valid password. Also, she is given special instructions about password choose based on the password she has entered.

```.py
def password_check(passwd: str):
    '''
    Password validation. Simply validates if the password meet valid password conditions.
    :param passwd: str
    :return: Bool
    '''

    SpecialSym =['$', '@', '#', '%', '!', '.', ',']
    # Creating a list with the symbols that the user can use in a password
    val = True

    # Checking if the user has entered a password whose length is less than 6
    # If yes, the user will get a warning and has to reenter a new password
    if len(passwd) < 6:
        print('❌️Length must be at least 6')
        time.sleep(0.1) # waiting for 0.1 seconds
        val = False

    # Checking if the user has entered a password whose length is more than 20
    # If yes, the user will get a warning and has to reenter a new password
    if len(passwd) > 20:
        print('❌️Length must be not be greater than 20')
        time.sleep(0.1) # waiting for 0.1 seconds
        val = False
        
    # Checking if the user has entered a password which has a number character
    # If no, the user will get a warning and has to reenter a new password
    if not any(char.isdigit() for char in passwd):
        print('❌️Password must have at least one numeral')
        time.sleep(0.1) # waiting for 0.1 seconds
        val = False

    # Checking if the user has entered a password which has an uppercase letter
    # If no, the user will get a warning and has to reenter a new password
    if not any(char.isupper() for char in passwd):
        print('❌️Password must have at least one uppercase letter')
        time.sleep(0.1) # waiting for 0.1 seconds
        val = False

    # Checking if the user has entered a password which has an lowercase letter
    # If no, the user will get a warning and has to reenter a new password
    if not any(char.islower() for char in passwd):
        print('❌️Password must have at least one lowercase letter')
        time.sleep(0.1) # waiting for 0.1 seconds
        val = False

    # Checking if the user has entered a password which has a valid symbol
    # If no, the user will get a warning and has to reenter a new password
    if not any(char in SpecialSym for char in passwd):
        print('❌️Password must have at least one of the symbols $@#%!.,')
        time.sleep(0.1) # waiting for 0.1 seconds
        val = False
    if val:
        return val
```
### Testing the program
![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Project/Images/Testing%20password%20validation.png)

## Transaction history table
"Transaction history" is the second element of the menu. I thought being able to see your transactions would decrease my customer's problem of not being able to follow her transactions. The program uses spendings.csv and currency converter function to get data from spendings.csv and convert their value from BNB to USD. I thought being able to see the value in a daily used currency would make it easier for the customer to read the data. Also, the program prints datas of different categories in different colors so the customer can differentiate her transanctions easily.

```.py
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
```
### Testing the program
![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Project/Images/Testing%20transaction%20history.png)

# Proof of working
[Testing video](https://drive.google.com/file/d/1YKB-m7xLVrIu9fFxc53BAWyWXm5vmdVr/view) of the program to see if it works
