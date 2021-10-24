def square(l):
    number = []
    for i in l:
        number.append(i**2)
    return number 
numbers = list(range(1,100))
print(square(numbers))