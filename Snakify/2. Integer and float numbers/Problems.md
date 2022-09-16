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

## Day of week
### Statement
Let's count the days of the week as follows: 0 - Sunday, 1 - Monday, 2 - Tuesday, ..., 6 - Saturday. Given an integer K in the range 1 to 365, find the number of the day of the week for the K-th day of the year provided that this year's January 1 is Thursday.
### My code
```.py
a = int(input())
answer = a % 7 + 3
if answer == 7:
    answer = 0
elif answer == 8:
    answer = 1
elif answer == 9:
    answer = 2
print(answer)
```
### The result 
![](https://raw.githubusercontent.com/2024sabuhiabbasov/Unit-1/main/Snakify/2.%20Integer%20and%20float%20numbers/Images/Day%20of%20week.png)

## Digital clock
### Statement
Given the integer N - the number of minutes that is passed since midnight - how many hours and minutes are displayed on the 24h digital clock?

The program should print two numbers: the number of hours (between 0 and 23) and the number of minutes (between 0 and 59).

For example, if N = 150, then 150 minutes have passed since midnight - i.e. now is 2:30 am. So the program should print 2 30.
### My code
```.py
a = int(input())
print(str(a // 60), str(a % 60))
```
### The result 
![](https://raw.githubusercontent.com/2024sabuhiabbasov/Unit-1/main/Snakify/2.%20Integer%20and%20float%20numbers/Images/Digital%20clock.png)

## Century
### Statement
Given a year as a positive integer, print its century. Mind that the 20th century began on 1901 and ended on 2000.
### My code
```.py
year = int(input())
if year <= 100:
    print(1)
elif year % 100 == 0:
    print(year // 100)
else:
    print(year // 100 + 1)
```
### The result 
![](https://raw.githubusercontent.com/2024sabuhiabbasov/Unit-1/main/Snakify/2.%20Integer%20and%20float%20numbers/Images/Century.png)
