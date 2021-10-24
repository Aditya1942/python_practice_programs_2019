num1,Operator,num2 = input("enter a number (space) enter a Operator like {+,-,*,/} (space) enter another number:  ").split()
num1 = int(num1)
num2 = int(num2)
if Operator == "+":
    answer = (num1 + num2)
elif Operator == "-":
    answer = (num1 - num2)    
elif Operator == "*":
    answer = (num1 * num2)
elif Operator == "/":
    answer = float(num1 / num2)
print(answer)
lol = input()
