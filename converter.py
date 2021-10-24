
method = input("1: binary to octal\n2: binary to dicimal\n3:binary to Hexadecimal: ")
binary = input("Enter any number in Binary Format: ")
if method=='1':
    temp = int(binary, 2)
    print(binary,"in Octal =",oct(temp))
elif method=='2':
    decimal = int(binary, 2)
    print(binary,"in Decimal =",decimal)
elif method=="3":
    temp = int(binary, 2)
    print(binary,"in Hexadecimal =",hex(temp))