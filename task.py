def task_1(numbers, N): # Numbers is a list of integer values, times is how many times to operatate (int)
    x = 0
    for number in numbers:
        for i in range(N):
            if number % 2 == 1:
                numbers[x] += 2
            elif number % 2 == 0:
                numbers[x] -= 2
        x += 1
    return numbers

def task_2(N): # N is any integer value
    msg = ""
    msg += "The most "
    if N % 1 == 0:
        msg += "brilliant "
    if N % 2 == 0:
        msg += "exciting "
    if N % 3 == 0:
        msg += "fantastic "
    if N % 4 == 0:
        msg += "virtuous "
    if N % 5 == 0:
        msg += "heart-warming "
    if N % 6 == 0:
        msg += "tear-jerking "
    if N % 7 == 0:
        msg += "beautiful "
    if N % 8 == 0:
        msg += "exhilarating "
    if N % 9 == 0:
        msg += "emotional "
    if N % 10 == 0:
        msg += "inspiring "
    msg += f"number is {N}!"
    return msg

def task_3(calc): # Calc is a string
    num1 = ""
    num2 = ""
    operator = ""
    number = 1
    for x in calc:

        if x == " ":
            continue
        if x == "+" or x == "-" or x == "*" or x == "/":
            number = 2
            operator += x
            continue
        if number == 1:
            num1 += x
        else:
            num2 += x
    num1 = int(num1)
    num2 = int(num2)
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "//":
        if num1 == 0 or num2 == 0:
            result = -1
        else:
            result = num1 // num2
    else:
        result = "ERROR: You may have formatted your input incorrectly"
    return result # Result should be a number answer
