while True: 
    name,character = input("enter your name and one character of your name: ").split()
    print(f"lenth of your name is {len(name)} ")
    print(f"character count: {name.lower().count(character.lower())}")