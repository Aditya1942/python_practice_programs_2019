while True:
    print(' who are you?')
    name=input()
    if name != 'aditya':
        continue
    print('hello, aditya. what is the password?')
    password=input()
    if password == 'prototype':
        print('welcome')
        break
