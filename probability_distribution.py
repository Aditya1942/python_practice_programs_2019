print("enter value of which you have and put 0 in rest ")
n = int(input("enter the value of N: "))
p = float(input("enter the value of p: "))
q = float(input("enter the value of q: "))
np = float(input("enter the value of np: "))
npq = float(input("enter the value of npq: "))
if n == 0:
    n = (np / p)
print(n)
if p == 0:
    p == 1-q
    if q == 0:
        npq 