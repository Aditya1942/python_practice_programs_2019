def cube_finder(n):
    spam = {}
    for i in range(1,n+1):
        spam[i] = i**3
    print(spam)

while True:
    a = input()
    a = int(a)
    cube_finder(a)
