D = {"Jan": 31, "Feb": 28, "Mar": 31, "Apr": 30, "May": 31, "Jun": 30,
     "Jul": 31, "Aug": 31, "Sept": 30, "Oct": 31, "Nov": 30, "Dec": 31, }

#  1
mon = input()
print(D[mon])

# 2
for i in sorted(D.keys()):
    print(i)

# 3
for i in D:
    if(D[i] == 31):
        print(i)
# 4
for i in sorted(D.keys()):
    print(f"{i}:{D[i]}")

# 5

# for i in sorted(D.values()):
#     print(f"{i}:{D[i]}")
