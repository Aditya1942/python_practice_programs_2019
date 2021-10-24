def odd_even(l):
    even = l[0::2]
    odd = l[1::2]
    return list([odd] + [even])

spam = list(range(0,8))
print(odd_even(spam))
a = input()