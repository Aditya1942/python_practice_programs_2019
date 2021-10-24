print("***************  instruction  *************** \n This program will find probability \n information needed: first of all enter how many x are there \np = probablity of sucess \nq = probablity of failuar\nn = number of outcome\nand r = x.\n enter \"exit\" to exit. ")
i = input("please enter how many x your have: ")
if i == "exit":
    exit()
while True:
    p = float(input("enter the value of p: "))
    q = float(input("enter the value of q: "))
    if i == "":
        break
    elif p + q != 1:
        print("wrong value inputed of q and p")
        continue

    import math
    spam1 = input("enter n: ")
    if spam1 == "exit":
        exit()
    else:
        spam2 = input("enter x: ")
        n = int(spam1)
        x = int(spam2)
        npr = math.factorial(n)/math.factorial(n-x)
        ncr = npr/math.factorial(x)
    if spam2 >= spam1:
        print("check the value of n and x carefully")
        continue
    

    second_step = p ** x

        
    third_step = q ** (n -x)

    a = ncr * (second_step * third_step)
    if i == "1":
        print(f"P(1) = {a}")
    elif i >= "2":
        print(f"P(1) = {a}")
        for l in range(1,5):
            print("*")
        print("enter n and x again using other value of x ")
        spam1 = input("enter n: ")
    if spam1 == "exit":
        exit()
    else:
        spam2 = input("enter x: ")
        n = int(spam1)
        x = int(spam2)
        npr = math.factorial(n)/math.factorial(n-x)
        ncr = npr/math.factorial(x)
    
    

    second_step = p ** x

        
    third_step = q ** (n -x)

    b = a + (ncr * second_step * third_step)
    if i == "2":
        print(f"P(1) + P(2) = {b}")
    elif i >= "3":
        print(f"P(1) + P(2) = {b}")
        for l in range(1,5):
            print("*")
        print("enter n and x again using other value of x ")
        spam1 = input("enter n: ")
    if spam1 == "exit":
        exit()
    else:
        spam2 = input("enter x: ")
        n = int(spam1)
        x = int(spam2)
        npr = math.factorial(n)/math.factorial(n-x)
        ncr = npr/math.factorial(x)
    
    

    second_step = p ** x

        
    third_step = q ** (n -x)

    c = b +  (ncr * second_step * third_step)
    if i == "3":
        print(f"P(1) + P(2) + P(3) = {c}")
    elif i >= "4":
        print(f"P(1) + P(2) x P(3) = {c}")
        for l in range(1,5):
            print("*")
        print("enter n and x again using other value of x ")
        spam1 = input("enter n: ")
    if spam1 == "exit":
        exit()
    else:
        spam2 = input("enter x: ")
        n = int(spam1)
        x = int(spam2)
        npr = math.factorial(n)/math.factorial(n-x)
        ncr = npr/math.factorial(x)
    
    

    second_step = p ** x

        
    third_step = q ** (n -x)

    d = c +  (ncr * second_step * third_step)
    if i == "4":
        print(f"P(1) + P(2) + P(3) + P(4) = {d}")
    elif i >= "5":
        print(f"P(1) + P(2) + P(3) + P(4) = {d}")
        for l in range(1,5):
            print("*")
        print("enter n and x again using other value of x ")
        spam1 = input("enter n: ")
    if spam1 == "exit":
        exit()
    else:
        spam2 = input("enter x: ")
        n = int(spam1)
        x = int(spam2)
        npr = math.factorial(n)/math.factorial(n-x)
        ncr = npr/math.factorial(x)
    
    

    second_step = p ** x

        
    third_step = q ** (n -x)

    e = d +  (ncr * second_step * third_step)
    if i == "5":
        print(f"P(1) + P(2) + P(3) + P(4) + P(5) = {e}")

