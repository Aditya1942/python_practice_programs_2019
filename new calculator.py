while True:
    num1,operation,num2 = input("enter your sum put space between numbers and operators ").split()
    if operation == "+":
        print(int(num1) + int(num2))
    elif operation == "-":
        print(int(num1) - int(num2))
    elif operation == "*":
        print(int(num1) * int(num2))
    elif operation == "/":
        print(float(num1) / float(num2))
    else:
        print("something is wrong \nuse a operation betweem number1 and number2 for example +,-,* and /")