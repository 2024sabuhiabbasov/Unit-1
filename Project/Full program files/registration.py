# New user registration

import csv

username = input("Please enter a username: ")
password = input("Please choose a password: ")
passConf = input("Please enter the password again to complete the registration: ")

while password != passConf:
    password = input("Passwords don't match, please enter again: ")
    passConf = input("Please enter again to complete the registration: ")

if password == passConf:
    with open('users.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(username)
        file.close()
    print(f"Registration successful. Welcome, {username}!")
