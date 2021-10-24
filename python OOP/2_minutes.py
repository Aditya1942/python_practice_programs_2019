
class Mth:
    @staticmethod
    def Minute(seconds):
        m = seconds//60
        s = seconds % 60
        print(m, " Minutes ", s, "Seconds")


maths = Mth()
maths.Minute(10000)
