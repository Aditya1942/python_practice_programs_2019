while True:
    print("this proggram will do sum of numbers ")          # this proggram will calculate from num1 to num2 which you have enter 
    num1 = int(input("enter a number: "))                   # for e.g num1 = 10 and num2 = 20 then it will calculate form 10 to 20 
    num2 = int(input("enter another number: "))             # 10+11+12+13.....+20 
    total = num1
    i = 1
    while i <=num2:
        total += i
        i += 1
    print(total)
