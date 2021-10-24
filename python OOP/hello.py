class Mth:
    def __init__(self):
        print("hello World INIT")

    def say_hello(self, loop):
        for i in range(1, loop+1):
            print("hello World", i)


maths = Mth()

maths.say_hello(47)
