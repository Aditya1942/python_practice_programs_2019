# 123-123-1234
number = input("Input number")
isvalid = True
if(len(number) != 12):
    isvalid = False
if(number[3] != "-" or number[7] != "-"):
    isvalid = False
for i in range(12):
    if(i == 3 or i == 7):
        continue
    if(not(number[i].isdigit())):
        isvalid = False
print(isvalid)
