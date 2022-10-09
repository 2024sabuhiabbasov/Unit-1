import time
import datetime
import json
import requests

def BNBconverter(spendingAmount: int)->int:
    key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    data = requests.get(key)
    data = data.json()
    return int(float(data['price'])) * spendingAmount

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
        num = input(f"{red}Wrong input!{end_code} {prompt}{end_code}")

    return int(num)

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

def simple_login(user: str, password: str)-> bool:
    '''
    Simple authentication, needs file users.csv
    :param user: string
    :param password: string
    :return: True/False if user is/not in database
    '''

    with open("users.csv") as file:
        database = file.readlines()
    output = False
    for line in database:
        line_cleaned = line.strip() # remove \n
        user_pass = line_cleaned.split(",")
        if user == user_pass[0] and password == user_pass[1]:
            output = True
            break
        file.close()
    return output

def userName(user: str, password: str)-> str:
    '''
    Finding user's first name by using the file users.csv
    :param user: string
    :param password: string
    :return: The user's first name
    '''
    with open("users.csv") as file:
        database = file.readlines()
    output = ""
    for line in database:
        line_cleaned = line.strip() # remove \n
        user_info = line_cleaned.split(",")
        if user == user_info[0] and password == user_info[1]:
            output = user_info[2]
            break
        file.close()
    return output

def LastName(user: str, password: str)-> str:
    '''
    Finding user's last name by using the file users.csv
    :param user: string
    :param password: string
    :return: The user's last name
    '''
    with open("users.csv") as file:
        database = file.readlines()
    output = ""
    for line in database:
        line_cleaned = line.strip() # remove \n
        user_info = line_cleaned.split(",")
        if user == user_info[0] and password == user_info[1]:
            output = user_info[3]
            break
        file.close()
    return output

def account_date(user: str, password: str)-> str:
    '''
    Finding user's account's creation date by using the file users.csv
    :param user: string
    :param password: string
    :return: The user's account's creation date
    '''
    with open("users.csv") as file:
        database = file.readlines()
    output = ""
    for line in database:
        line_cleaned = line.strip() # remove \n
        user_info = line_cleaned.split(",")
        if user == user_info[0] and password == user_info[1]:
            output = user_info[4]
            break
        file.close()
    return output
