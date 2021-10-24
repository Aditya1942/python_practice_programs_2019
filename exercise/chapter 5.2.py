
def reverse_str(l):
    a = l[0][::-1]
    b = l[1][::-1]
    c = l[2][::-1]
    return [a, b, c]
spam = list(["abc", "tuv", "xyz"])
print(reverse_str(spam))
a = input()