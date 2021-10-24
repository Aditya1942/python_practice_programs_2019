n = int(input())
if not n%2 == 0:
    print("werid")
elif n >= 6 and n <= 20 and n%2 == 0:
    print("weird")
elif n > 21 or n <= 5 and n%2 == 0:
    print("not werid")
