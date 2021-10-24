while True: 
    def  grater_number(a,b,c):
        if a>b and a>c:
            return (f"{a} is greater than {b} and {c} ")
        elif b>a and b>c:
            return (f"{b} is greater than {a} and {c} ")
        else:
            return (f"{c} is greater than {a} and {b} ")
    a = input("enter 3 numbers one by one: ")
    b = input("enter second number: ")
    c = input("enter third number: ")



    print(grater_number(a,b,c))