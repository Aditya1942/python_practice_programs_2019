
print('p = probablity of sucess \nq = probablity of failuar\nn = number of outcome\nand r = x. ')
print('press \"s\" for exit.')

p = float(input("enter the value of p: "))
q = float(input("enter the value of q: "))


import math
spam1 = input("enter n: ")
if spam1 == "s":
    exit()

else:
    spam2 = input("enter x: ")
    n = int(spam1)
    x = int(spam2)
    npr = math.factorial(n)/math.factorial(n-x)
    ncr = npr/math.factorial(x)
 

second_step = p ** x

    
third_step = q ** (n -x)

Answer = ncr * second_step * third_step
print(f"your answer is {Answer}")