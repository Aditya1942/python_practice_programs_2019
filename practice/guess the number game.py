while True:
    import random
    secret_number = random.randint(1, 20)
    print("i\'m thinking of a number can you guess it.")
    for guesstaken in range(1,7):
        print("take a guess")
        guess = int(input())
        if guess < secret_number:
            print("your guess is too low.")
        elif guess > secret_number:
            print("your guess is too high.")
        else:
            break
    if guess == secret_number:
        print(f"good job you guess the number in  {str(guesstaken)} guesses")
    else:
        print(f"nope the number is {secret_number}")
    print("try again")   
