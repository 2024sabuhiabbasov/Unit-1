#simople_login.py
from getpass import getpass

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

    return output

end_code = "\033[00m"
colors = ['\33[0;30m', '\33[1;31m', '\33[0;32m', '\33[0;33m', '\33[0;34m', '\33[0;35m', '\33[0;36m']

name = input(colors[3] + "Please enter username to continue: " + end_code)
password = input(colors[3] + "Please enter password to login: " + end_code)

checker = simple_login(name, password)
while checker == False:
    print(colors[1] + "Wrong username or password. Please try again!" + end_code)
    name = input(colors[3] + "Please enter username again to continue: " + end_code)
    password = input(colors[3] + "Please enter password again to login: " + end_code)
    checker = simple_login(name, password)

if checker == True:
    print(colors[2] + "Successful login!" + end_code)
