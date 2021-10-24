birthday = {"aditya":"feb 28"}
while True:
    print("enter a name : (blank to quit)")
    name = input()
    if name == '':
        break       
    if name in birthday:
        print(f"{birthday[name]} is the birthday of {name}")
    else:
        print(f"i do not have birthday information for {name} ")
        print("what is there birthday?")
        bday = input()
        birthday[name] = bday
        if bday == "":
            break
        print("birthday database is updated")