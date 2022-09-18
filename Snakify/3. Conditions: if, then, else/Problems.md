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
