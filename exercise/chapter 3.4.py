import random
while True:
    secrate_number = random.randint(1,100)
    print("i am guessing a number between 1 to 100 take a guess")
    i = 1
    number = int(input("enter a number: "))
    game_over = False
    while not game_over:
        if number == secrate_number:
            print(f"you win, you guess the number in {i}")
            game_over = True
        elif number >= 101:
            print("i said between 1 to 100 you enter number gratter than 100")
            i += 1
            number = int(input("try again: "))       
        else:
            if number < secrate_number:
                print("too low")
            else:
                print("too high")
            i += 1
            number = int(input("try again: "))