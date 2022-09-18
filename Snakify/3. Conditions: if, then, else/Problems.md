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

## Digits in ascending order
### Statement
Given a three-digit integer, print YES if its digits go in ascending order, print NO otherwise.
### My code
```.py
a = int(input())
f = a // 100
s = (a // 10) % 10
t = a % 10
if f <= s and s <= t:
    print("YES")
else:
    print("NO")
```
### The result 
![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Snakify/3.%20Conditions:%20if%2C%20then%2C%20else/Images/Digits%20in%20ascending%20order.png)

## Four-digit palindrome
### Statement
A palindrome is a number which reads the same when read forward as it it does when read backward. Given a four-digit integer, print "YES" if it's a palindrome and print "NO" otherwise.
### My code
```.py
a = int(input()) ## 1234
f = a // 1000
s = (a // 100) % 10
t = (a // 10) % 10
l = a % 10
if f == l and s == t:
    print("YES")
else:
    print("NO")
```
### The result 
![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Snakify/3.%20Conditions:%20if%2C%20then%2C%20else/Images/Four-digit%20palindrome.png)

## King move
### Statement
Chess king moves horizontally, vertically or diagonally to any adjacent cell. Given two different cells of the chessboard, determine whether a king can go from the first cell to the second in one move.

The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a king can go from the first cell to the second in one move, or NO otherwise.
### My code
```.py
c1 = int(input())
r1 = int(input())
c2 = int(input())
r2 = int(input())

if r2 - r1 == 1:
    if c1 == c2:
        print("YES")
    elif c1 == c2 - 1:
        print("YES")
    elif c1 == c2 + 1:
        print("YES")
    else:
        print("NO")
        
elif r2 + 1 == r1:
    if c1 == c2:
        print("YES")
    elif c1 == c2 - 1:
        print("YES")
    elif c1 == c2 + 1:
        print("YES")
    else:
        print("NO")

elif c2 - c1 == 1:
    if r1 == r2:
        print("YES")
    elif r1 == r2 - 1:
        print("YES")
    elif r1 == r2 + 1:
        print("YES")
    else:
        print("NO")
        
elif c2 + 1 == c1:
    if r1 == r2:
        print("YES")
    elif r1 == r2 - 1:
        print("YES")
    elif r1 == r2 + 1:
        print("YES")
    else:
        print("NO")
        
else:
    print("NO")
```
### The result 
![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Snakify/3.%20Conditions:%20if%2C%20then%2C%20else/Images/King%20move.png)

## Bishop moves
### Statement
In chess, the bishop moves diagonally, any number of squares. Given two different squares of the chessboard, determine whether a bishop can go from the first to the second in one move.

The program receives as input four numbers from 1 to 8, specifying the column and row numbers of the starting square and the column and row numbers of the ending square. The program should output YES if a Bishop can go from the first square to the second in one move, or NO otherwise.
### My code
```.py
c1 = int(input())
r1 = int(input())
c2 = int(input())
r2 = int(input())

if ((r2 - r1 == c2 - c1) or (c1 == r2 and r1 == c2)) or (c2 - c1 == r1 - r2 or c1 - c2 == r2 - r1):
    print("YES")
else:
    print("NO")
```
### The result 
![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Snakify/3.%20Conditions:%20if%2C%20then%2C%20else/Images/Bishop%20moves.png)

## Queen move
### Statement
Chess queen moves horizontally, vertically or diagonally to any number of cells. Given two different cells of the chessboard, determine whether a queen can go from the first cell to the second in one move.

The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a queen can go from the first cell to the second in one move, or NO otherwise.
### My code
```.py
c1 = int(input())
r1 = int(input())
c2 = int(input())
r2 = int(input())
if abs(c1 - c2) == abs(r1 - r2):
    print("YES")
elif c1 == c2 or r1 == r2:
    print("YES")
else:
    print('NO')
```
### The result 
![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Snakify/3.%20Conditions:%20if%2C%20then%2C%20else/Images/Queen%20move.png)

## Index of outlier
### Statement
Given three integers: two are equal to each other and the third one is different. Print the index number of this different one - 1, 2 or 3.
### My code
```.py
a = int(input())
b = int(input())
c = int(input())

if a == b:
    print(3)
elif a == c:
    print(2)
else:
    print(1)
```
### The result 
![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Snakify/3.%20Conditions:%20if%2C%20then%2C%20else/Images/Index%20of%20outlier.png)

## Knight move
### Statement
Chess knight moves like the letter L. It can move two cells horizontally and one cell vertically, or two cells vertically and one cells horizontally. Given two different cells of the chessboard, determine whether a knight can go from the first cell to the second in one move.

The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a knight can go from the first cell to the second in one move, or NO otherwise.
### My code
```.py
c1 = int(input())
r1 = int(input())
c2 = int(input())
r2 = int(input())

if abs(c1 - c2) == 2 and abs(r1 - r2) == 1:
    print("YES")
elif abs(c1 - c2) == 1 and abs(r1 - r2) == 2:
    print("YES")
else:
    print("NO")
```
### The result 
![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Snakify/3.%20Conditions:%20if%2C%20then%2C%20else/Images/Knight%20move.png)

## Chocolate bar
### Statement
Chocolate bar has the form of a rectangle divided into n×m portions. Chocolate bar can be split into two rectangular parts by breaking it along a selected straight line on its pattern. Determine whether it is possible to split it so that one of the parts will have exactly k squares.

The program reads three integers: n, m, and k. It should print YES or NO.
### My code
```.py
n = int(input())
m = int(input())
k = int(input())

if k <= (n * m) and (k % n == 0 or k % m == 0):
    print("YES")
else:
    print("NO")
```
### The result 
![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Snakify/3.%20Conditions:%20if%2C%20then%2C%20else/Images/Chocolate%20bar.png)

## Leap year
### Statement
Given the year number. You need to check if this year is a leap year. If it is, print LEAP, otherwise print COMMON.
The rules in Gregorian calendar are as follows:

a year is a leap year if its number is exactly divisible by 4 and is not exactly divisible by 100
a year is always a leap year if its number is exactly divisible by 400

Warning. The words LEAP and COMMON should be printed all caps.
### My code
```.py
year = int(input())

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("LEAP")
else:
    print("COMMON")
```
### The result 
![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Snakify/3.%20Conditions:%20if%2C%20then%2C%20else/Images/Leap%20year.png)

## Days in month
### Statement
Given a month - an integer from 1 (January) to 12 (December), print the number of days in it in the year 2017 (or any other non-leap year).
### My code
```.py
month = int(input())
days = ["31", "28", "31", "30", "31", "30", "31", "31", "30", "31", "30", "31"]
print(days[month - 1])
```
### The result 
![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Snakify/3.%20Conditions:%20if%2C%20then%2C%20else/Images/Days%20in%20month.png)

## Linear equation
### Statement
Write a program that solves a linear equation ax = b in integers. Given two integers a and b (a may be zero), print a single integer root if it exists and print "no solution" or "many solutions" otherwise.
### My code
```.py
a = int(input())
b = int(input())

if abs(a) > abs(b) or (a == 0 and b != 0):
    print("no solution")
elif a == 0 and b == 0:
    print("many solutions")
else:
    print(b//a)
```
### The result 
![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Snakify/3.%20Conditions:%20if%2C%20then%2C%20else/Images/Linear%20equation.png)

## Sort three numbers
### Statement
Given three integers, print them in ascending order.
### My code
```.py
a = int(input())
b = int(input())
c = int(input())
mi = min(a, min(b, c))
ma = max(a, max(b, c))
m = (a + b + c) - mi - ma
print(mi, m, ma)
```
### The result 
![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Snakify/3.%20Conditions:%20if%2C%20then%2C%20else/Images/Sort%20three%20numbers.png)

## White pawn move
### Statement
A white chess pawn moves up vertically one square at a time. An exception is a pawn on a row #2: it can move either one or two squares up. In addition, a white chess pawn captures diagonally up one square to the left or right. A white chess pawn can never occur on a row #1.

The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first square, and then the last two - for the second square. The program should print YES if a white pawn can possibly move from the first square to the second square in one move in some game - either by move or by capture. The program should print NO otherwise. The first four tests correspond to the green arrows on the picture below.
### My code
```.py
c1 = int(input())
r1 = int(input())
c2 = int(input())
r2 = int(input())

if r1 == 1 or r2 == 1:
    print("NO")

elif c1 == c2:
    if r2 - r1 == 1:
        print("YES")
    elif r1 == 2 and r2 == 4:
        print("YES")
    else:
        print("NO")
        
elif abs(c1 - c2) == 1:
    if abs(r2 - r1) == 1:
        print("YES")
    else:
        print("NO")
        
else:
    print("NO")
```
### The result 
![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Snakify/3.%20Conditions:%20if%2C%20then%2C%20else/Images/White%20pawn%20move.png)
