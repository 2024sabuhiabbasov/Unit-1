# Finished chapter
# 3. Conditions: if then, else
## Is positive
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

## Sum of digits
### Statement
Given a three-digit number. Find the sum of its digits.
### My code
```.py
a = int(input())
f = a // 100
s = (a // 10) % 10
t = a % 10
print(f + s + t)
```
### The result 
![](https://raw.githubusercontent.com/2024sabuhiabbasov/Unit-1/main/Snakify/2.%20Integer%20and%20float%20numbers/Images/Sum%20of%20digits.png)

## Reverse three digits
### Statement
Given a three-digit integer number, print its digits in a reversed order.
### My code
```.py
a = int(input())
f = a // 100
s = (a // 10) % 10
t = a % 10
print(str(t) + str(s) + str(f))
```
### The result 
![](https://raw.githubusercontent.com/2024sabuhiabbasov/Unit-1/main/Snakify/2.%20Integer%20and%20float%20numbers/Images/Reverse%20three%20digits.png)

## Merge two numbers
### Statement
Given two two-digit numbers, merge their digits as shown in the tests below.
### My code
```.py
a = int(input())
b = int(input())
f = a // 10
s = b // 10
t = a % 10
l = b % 10
print(str (f) + str (s) + str (t) + str (l))
```
### The result 
![](https://raw.githubusercontent.com/2024sabuhiabbasov/Unit-1/main/Snakify/2.%20Integer%20and%20float%20numbers/Images/Merge%20two%20numbers.png)

## Cyclic rotation
### Statement
Given a four-digit integer number, perform its cyclic rotation by two digits, as shown in the tests below.
### My code
```.py
a = int(input())
f = a // 10 % 10
s = a % 10
t = a // 1000
l = a //100 % 10
print(str (f) + str (s) + str (t) + str (l))
```
### The result 
![](https://raw.githubusercontent.com/2024sabuhiabbasov/Unit-1/main/Snakify/2.%20Integer%20and%20float%20numbers/Images/Cyclic%20rotation.png)

## Fractional part
### Statement
Given a positive real number, print its fractional part.
### My code
```.py
a = float(input())
print(a - int(a))
```
### The result 
![](https://raw.githubusercontent.com/2024sabuhiabbasov/Unit-1/main/Snakify/2.%20Integer%20and%20float%20numbers/Images/Fractional%20part.png)

## First digit after decimal point
### Statement
Given a positive real number, print its first digit to the right of the decimal point.
### My code
```.py
a = float(input())
print(int(a * 10) % 10)
```
### The result 
![](https://raw.githubusercontent.com/2024sabuhiabbasov/Unit-1/main/Snakify/2.%20Integer%20and%20float%20numbers/Images/First%20digit%20after%20decimal%20point.png)

## Car route
### Statement
A car can cover distance of N kilometers per day. How many days will it take to cover a route of length M kilometers? The program gets two numbers: N and M.
### My code
```.py
n = int(input())
m = int(input())
ans = int(m // n)
if m % n != 0:
   ans += 1
print(ans)
```
### The result 
![](https://raw.githubusercontent.com/2024sabuhiabbasov/Unit-1/main/Snakify/2.%20Integer%20and%20float%20numbers/Images/Car%20route.png)
