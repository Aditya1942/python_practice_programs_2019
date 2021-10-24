lol = ["a", "b","c", "d", "e", "f", "g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
num = list(range(1,11))
count = 0
while count < 26:
    count2 = 0
    while count2 < 10:
        print(f"{lol[count]}{num[count2]}", end=" > ")
        count2 += 1
        if count2 == 10:
            count += 1
        