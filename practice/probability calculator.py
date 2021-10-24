import pprint
for i in range(100):
    lol = (i)
    print(lol)  
    pprint.pformat(f"hello world {i}")
import os 
spam = open("h:\\[1] my games\\python programs\\spam.txt", "w")
spam.write(pprint.pformat(f"hello world {i}"))