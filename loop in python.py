a = input("enter the value of a: ")
b = input("enter the value of b: ")
a = int(a)
b = int(b)
lis = ["one","two","three","four","five","six","seven","eight","nine"]

for i in range(a-1,b):
        if i == 9:
            break
        print(lis[i])

if b >=10 and i==9:
    for j in range(i,b):
        if j%2==0:
            print("even")
        else:
            print("odd")


