## Quiz 003
**Statement**

Create a program that translate the proteins in the DNA chain as shown below. [HL]  Input is a whole protein chain as a string.

**Example**
![](https://raw.githubusercontent.com/2024sabuhiabbasov/Unit-1/main/Quizzes/Images/Quiz%20003%20-%20test.png)

**My code**
```.py
# The program translates the proteins in the DNA chain

protein_name = input()
new = list(protein_name)

for i in range(0, len(protein_name)):
    if protein_name[i] == 'A':
        new[i] = 'T'
    elif protein_name[i] == 'G':
        new[i] = 'C'
    elif protein_name[i] == 'T':
        new[i] = 'A'
    elif protein_name[i] == 'C':
        new[i] = 'G'
    else:
        print('Please enter an invalid protein symbol.')
        exit()
    ''.join(new)

for i in range(0, len(protein_name)):
    print(new[i], end='')

```
**Test**

![](https://raw.githubusercontent.com/2024sabuhiabbasov/Unit-1/main/Quizzes/Images/Quiz%20003.png)
