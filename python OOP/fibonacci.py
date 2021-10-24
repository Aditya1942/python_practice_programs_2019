L = [1, 1]
for i in range(8):
    s = L[i] + L[i+1]
    L.append(s)
print(L)