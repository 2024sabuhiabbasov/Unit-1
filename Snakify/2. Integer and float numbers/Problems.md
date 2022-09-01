# 2. Integer and float numbers
## Last digit of integer
### Statement
Given an integer number, print its last digit.

Remember that you can convert the numbers to strings using the function str.
### My code
```.py
a = int(input())
print(a % 10)
```
### The result 
![](https://raw.githubusercontent.com/2024sabuhiabbasov/Unit-1/main/Snakify/2.%20Integer%20and%20float%20numbers/Images/Last%20digit%20of%20integer.png)

## Two digits
### Statement
Given a two-digit number, print its digits separately.
### My code
```.py
a = int(input())
print(a // 10 , a % 10)
```
### The result 
![](https://raw.githubusercontent.com/2024sabuhiabbasov/Unit-1/main/Snakify/2.%20Integer%20and%20float%20numbers/Images/Two%20digits.png)

## Swap digits
### Statement
Given a two-digit number, swap its digits as shown in the tests below.
### My code
```.py
a = int(input())
print(str(a % 10) + str(a // 10))
```
### The result 
![](https://raw.githubusercontent.com/2024sabuhiabbasov/Unit-1/main/Snakify/2.%20Integer%20and%20float%20numbers/Images/Swap%20digits.png)

## Last two digits
### Statement
Given an integer number, print its last two digits.
### My code
```.py
a = int(input())
print(str(a % 100))
```
### The result 
![](https://raw.githubusercontent.com/2024sabuhiabbasov/Unit-1/main/Snakify/2.%20Integer%20and%20float%20numbers/Images/Last%20two%20digits.png)

## Tens digit
### Statement
Given an integer. Print its tens digit.
### My code
```.py
a = int(input())
print((a // 10) % 10)
```
### The result 
![](https://raw.githubusercontent.com/2024sabuhiabbasov/Unit-1/main/Snakify/2.%20Integer%20and%20float%20numbers/Images/Tens%20digit.png)
