# Exercise 3
**Statement**

Write a program to sort alphabetically three names entered by the user. Note: **Assume that only the first letter of names are the same.**

### My code
```.py
# The program sorts there names alphabetically entered by the user

listOfNames = []

for i in range(0, 3):
    name = input() # We get a name from the user
    listOfNames.append(name) # We add the entered name to the list

newList = sorted(listOfNames) # By using sorted function, we sort the ames alphabetically

for i in range(0, 3):
    print(newList[i]) # We print entered names

```
