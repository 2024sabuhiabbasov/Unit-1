# Finished chapter
# 3. Conditions: if then, else
## Is positive
### Statement
Given an integer, print "YES" if it's positive and print "NO" otherwise.
### My code
```.py
a = int(input())
if a > 0:
    print("YES")
else:
    print("NO")
```
### The result 
![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Snakify/3.%20Conditions:%20if%2C%20then%2C%20else/Images/Is%20positive.png)

## Is odd
### Statement
Given an integer, print "YES" if it's odd and print "NO" otherwise.
### My code
```.py
a = int(input())
if a % 2 == 1:
    print("YES")
else:
    print("NO")
```
### The result 
![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Snakify/3.%20Conditions:%20if%2C%20then%2C%20else/Images/Is%20odd.png)

## Is even
### Statement
Given an integer, print "YES" if it's even and print "NO" otherwise.
### My code
```.py
a = int(input())
if a % 2 == 0:
    print("YES")
else:
    print("NO")
```
### The result 
![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Snakify/3.%20Conditions:%20if%2C%20then%2C%20else/Images/Is%20even.png)

## Ends on seven
### Statement
Given an integer, print "YES" if it's last digit is 7 and print "NO" otherwise.
### My code
```.py
a = int(input())
if a % 10 == 7:
    print("YES")
else:
    print("NO")
```
### The result 
![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Snakify/3.%20Conditions:%20if%2C%20then%2C%20else/Images/Ends%20on%20seven.png)

## Minimum of two numbers
### Statement
Given two integers, print the smaller value.
### My code
```.py
a = int(input())
b = int(input())
if a >= b:
    print(b)
else:
    print(a)
```
### The result 
![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Snakify/3.%20Conditions:%20if%2C%20then%2C%20else/Images/Minimum%20of%20two%20numbers.png)

## Are both odd
### Statement
Given two integers, print "YES" if they're both odd and print "NO" otherwise.
### My code
```.py
a = int(input())
b = int(input())
if a % 2 == 1:
    if b % 2 == 1:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
```
### The result 
![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Snakify/3.%20Conditions:%20if%2C%20then%2C%20else/Images/Are%20both%20odd.png)

## At least one odd
### Statement
Given two integers, print "YES" if at least one of them is odd and print "NO" otherwise.
### My code
```.py
a = int(input())
b = int(input())
if a % 2 == 1 or b % 2 == 1:
    print("YES")
else:
    print("NO")
```
### The result 
![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Snakify/3.%20Conditions:%20if%2C%20then%2C%20else/Images/At%20least%20one%20odd.png)

## Exactly one odd
### Statement
Given two integers, print "YES" if exactly one of them is odd and print "NO" otherwise.
### My code
```.py
a = int(input())
b = int(input())
if (a % 2 == 1 and b % 2 != 1) or (b % 2 == 1 and a % 2 != 1):
    print("YES")
else:
    print("NO")
```
### The result 
![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Snakify/3.%20Conditions:%20if%2C%20then%2C%20else/Images/Exactly%20one%20odd.png)

## Sign function
### Statement
For the given integer X print 1 if it's positive, -1 if it's negative, or 0 if it's equal to zero.
Try to use the cascade if-elif-else for it.
### My code
```.py
a = int(input())
if a > 0:
    print(1)
elif a < 0:
    print(-1)
else:
    print(0)
```
### The result 
![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Snakify/3.%20Conditions:%20if%2C%20then%2C%20else/Images/Sign%20function.png)

## Numbers in ascending order
### Statement
Given three different integers, print YES if they're given in ascending order, print NO otherwise.
### My code
```.py
a = int(input())
b = int(input())
c = int(input())
if a < b and b < c:
    print("YES")
else:
    print("NO")
```
### The result 
![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Snakify/3.%20Conditions:%20if%2C%20then%2C%20else/Images/Numbers%20in%20ascending%20order.png)

## Is three digit
### Statement
Given an integer, print "YES" if it's a three-digit number and print "NO" otherwise.
### My code
```.py
a = int(input())
if a >= 100 and a <= 999:
    print("YES")
else:
    print("NO")
```
### The result 
![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Snakify/3.%20Conditions:%20if%2C%20then%2C%20else/Images/Is%20three%20digit.png)
