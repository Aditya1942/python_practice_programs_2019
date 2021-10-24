while True:
    n = input("enter any numbers: ")     # this proggram calculate number like for e.g 1234 = 1+2+3+4
    total = 0 
    i = 0
    while i < len(n):
        total += int(n[i])
        i += 1
    print(total)