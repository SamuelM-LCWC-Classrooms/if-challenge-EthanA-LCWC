[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=16105471)
# If challenge

Each of the challenges below will be autograded by a number of tests - your total score will be out of 12

Note, for this challenege you may use if statements, for and while loops

## Task 1 - Up and Down Numbers

You have a code which will read in two values, the first will be a list of numbers, the second will be an integer value

Your program must perform an even-odd transfrom to the list of numbers for N times, N is the integer value passed to the code

The transformation follows these rules:
* Add 2 (+2) to numbers that are odd
* Subtract 2 (-2) to numbers that are even

For example:
```
    task_1([3, 4, 9], 3) = [9, -2, 15]
```

_Note - you do not need to use any user-inputs, the data input is automatically passed to the code_

## Task 2 - Brilliant, Exciting, Fantastic Numbers

Your code will read in an integer value N

Your code will then construct a messgae in the msg variable (string)

The code will follow the following rules:
1. Always start with "The most"
2. If N is divisible by 1, add "brilliant" to the sentence
3. If N is divisible by 2, add "exciting" to the sentence
4. ... 3, add "fantastic" to the sentence
5. ... 4, add "virtuous" to the sentence
6. ... 5, add "heart-warming"...
7. ... 6, add "tear-jerking" ...
8. ... 7, add "beautiful" ...
9. ... 8, add "exhilarating" ...
10. ... 9, add "emotional" ...
11. ... 10, add "inspiring to the sentence.
12. Always end the string with "number is" N! Where N is replaced by the number.

For example:
```
task_2(4) = "The most brilliant exciting virtuous number is 4!"
```

Remember you need to ensure it _exactly_ matches!

## Task 3 - Basic Arithmetic Operations on a String Number

Your code will read in a string of the form "num1 + num2" where num1 and num2 are replaced with number didgits (ints only)

The string will be one of four operations, +, -, *, //

Your code must use the string to find what the numbers are and perform the operation, storing the result as an integer value in the variable result

You may not use the eval() function

If there is a division by zero, have the value of result be set to -1

_Note - rather than normal division we are using floor division // - recall that this rounds down, removing the decimal_

For example:
```
task_3("12 + 12") = 24
task_3(12 // 0") = -1
```