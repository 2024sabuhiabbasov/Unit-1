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

## Minimum of three numbers
### Statement
Given three integers, print the smallest value.
### My code
```.py
a = int(input())
b = int(input())
c = int(input())
print(min(a, min(b, c)))
```
### The result 
![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Snakify/3.%20Conditions:%20if%2C%20then%2C%20else/Images/Minimum%20of%20three%20numbers.png)

## Equal numbers
### Statement
Given three integers, determine how many of them are equal to each other. The program must print one of these numbers: 3 (if all are the same), 2 (if two of them are equal to each other and the third is different) or 0 (if all numbers are different).
### My code
```.py
a = int(input())
b = int(input())
c = int(input())
if a == b and b == c:
    print(3)
elif a != b and b != c and a != c:
    print(0)
else:
    print(2)
```
### The result 
![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Snakify/3.%20Conditions:%20if%2C%20then%2C%20else/Images/Equal%20numbers.png)

## Rook move
### Statement
Chess rook moves horizontally or vertically. Given two different cells of the chessboard, determine whether a rook can go from the first cell to the second in one move.

The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a rook can go from the first cell to the second in one move, or NO otherwise.
### My code
```.py
x = int(input())
y = int(input())
x1 = int(input())
y1 = int(input())
if x == x1:
    print("YES")
elif y == y1:
    print("YES")
else:
    print("NO")
```
### The result 
![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Snakify/3.%20Conditions:%20if%2C%20then%2C%20else/Images/Rook%20move.png)

## Chess board - black square
### Statement
Given a square of a chessboard. Print BLACK if it's black and print WHITE otherwise.
The program receives two numbers from 1 to 8 each - the column and the row number of the square.
### My code
```.py
x = int(input())
y = int(input())
if x == y:
    print("BLACK")
elif x % 2 == 0:
    if y % 2 == 0:
        print("BLACK")
    else:
        print("WHITE")
elif x % 2 == 1:
    if y % 2 == 0:
        print("WHITE")
    else:
        print("BLACK")
```
### The result 
![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Snakify/3.%20Conditions:%20if,%20then,%20else/Images/Chess%20board%20-%20black%20square.png)

## Chess board - same color
### Statement
Given two cells of a chessboard. If they are painted in one color, print the word YES, and if in a different color - NO.
The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell.
### My code
```.py
x = int(input())
y = int(input())
x1 = int(input())
y1 = int(input())
s = 0;
s1 = 0;
if x == y:
    s = 0;
elif x % 2 == 0:
    if y % 2 == 0:
        s = 0;
    else:
        s = 1;
elif x % 2 == 1:
    if y % 2 == 0:
        s = 1;
    else:
        s = 0;
if x1 == y1:
    s1 = 0;
elif x1 % 2 == 0:
    if y1 % 2 == 0:
        s1 = 0;
    else:
        s1 = 1;
elif x1 % 2 == 1:
    if y1 % 2 == 0:
        s1 = 1;
    else:
        s1 = 0;
if s == s1:
    print("YES")
else:
    print("NO")
```
### The result 
![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Snakify/3.%20Conditions:%20if%2C%20then%2C%20else/Images/Chess%20board%20-%20same%20color.png)

## Distance to closest point
### Statement
Given the coordinates of the three points A, B, and C on a line. Print a distance from the point A to closest point to it.
### My code
```.py
a = int(input())
b = int(input())
c = int(input())
ans = min(abs(a-b), abs(a-c))
print(ans)
```
### The result 
![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Snakify/3.%20Conditions:%20if%2C%20then%2C%20else/Images/Distance%20to%20closest%20point.png)
