# Quiz 016
**Statement**

Create a function that produces the output given the input shown

## Test cases
![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Quizzes/Images/Quiz%20016%20-%20test%20cases.png)

## My solutions
### Code
```.py
import string
def blackBoxThree(given: str)->str:
    answer = ''
    count = []

    for letter in given.lower():
        if letter.isalpha():
            included = False
            for item in count:
                if item[0] == letter:
                    item[1] += 1
                    included = True
                    answer += str(item[1])
            if included == False:
                count.append([letter, 1])
                answer += '1'
        else:
            answer += letter

    return answer

given = input()

print(blackBoxThree(given))
```
### Flow diagram
![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Quizzes/Images/Quiz%20016%20-%20Flow%20diagram.jpg)

**Testing the code**

**Test 1**

![](https://github.com/2024sabuhiabbasov/Unit-1/blob/main/Quizzes/Images/Quiz%20016%20-%20testing%20the%20program.png)
