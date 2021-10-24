mycat = {"size":"fat", "color":"black", "dispostion": "loud"}
while True:
    spam = input()
    if spam == "":
        break
    elif spam in mycat:
        print(f"In terms of {spam}  \nMy cat is {mycat[spam]}. ")
    else:
        print("no this information is not available")